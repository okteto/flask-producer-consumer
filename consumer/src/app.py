import pika

from pymongo import MongoClient
import time
import os


task_queue = os.environ['TASK_QUEUE']

def wait_for_queue_connection():
    while True:
        try:
            credentials = pika.PlainCredentials(os.environ['RABBITMQ_USER'],
                                                os.environ['RABBITMQ_PASS'])
            params = pika.ConnectionParameters('rabbitmq', os.environ['RABBITMQ_PORT'], '/', credentials, heartbeat=0)
            connection = pika.BlockingConnection(params)
            break
        except Exception as ex:
            print("Consumer not connected to queue yet..")
            time.sleep(1)
    print("Connected")
    return connection


# Open connection to a rabbitMQ queue
connection = wait_for_queue_connection()
channel = connection.channel()
channel.queue_declare(queue=task_queue, durable=True)

# Open connection to a MongoDB collection
mongo_client = MongoClient('mongodb://mongodb:27017')
database = mongo_client.strings
collection = database.get_collection('to_uppercase')

def callback(ch, method, properties, body):

    lowercased = body.decode("utf-8")
    uppercased_body = lowercased.upper()
    collection.insert_one({"lower": lowercased, "uppercase": uppercased_body})
    print("Consumed 1")
    if channel.is_open:
        channel.basic_ack(method.delivery_tag)


if __name__ == '__main__':
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=task_queue, on_message_callback=callback)

    channel.start_consuming()

