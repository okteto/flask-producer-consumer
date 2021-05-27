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

@app.route('/db/initialized', methods=["GET"])
def initialized():
    print("enter in initialization")
    mongo_result = collection.find({ "uppercase": "FIRST MESSAGE" })
    print(mongo_result)
    if len(mongo_result) != 0:
        return "true"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
