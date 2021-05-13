from flask import Flask, request
from flask_api import status
from pymongo import MongoClient
from bson import json_util
import json

mongo_client = MongoClient('mongodb://mongodb:27017')
database = mongo_client.strings
collection = database.get_collection('to_uppercase')

app = Flask(__name__)

@app.route('/')
def alive():
    return "Hello-world"


@app.route('/db', methods=["GET"])
def get_data():
    sanitized = json.loads(json_util.dumps(collection.find_one()))
    return sanitized


@app.route('/db', methods=["DELETE"])
def delete_db():
    try:
        mongo_client.drop_database('patents')
        return {'message': 'deleted'}, status.HTTP_200_OK
    except Exception as ex:
        return {'message': str(ex)}, status.HTTP_500_INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(host='0.0.0.0')
