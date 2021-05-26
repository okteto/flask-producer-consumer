import pika
import time
import os
import random
import string

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
            print("Producer not connected to queue yet..")
            time.sleep(1)
    print("Connected")
    return connection


connection = wait_for_queue_connection()
channel = connection.channel()
channel.queue_declare(queue=task_queue, durable=True)
channel.basic_qos(prefetch_count=1)

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body= "First message")
print("Finished initalization")
