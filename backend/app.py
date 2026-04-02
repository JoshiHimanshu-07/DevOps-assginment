import os

from flask import Flask, request, jsonify
from flask.cli import load_dotenv
from pymongo import MongoClient


load_dotenv()
mongo_uri = os.getenv("client")
client = MongoClient(mongo_uri)

db = client["todoDB"]
collection = db["todoItems"]

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return jsonify({"message": "Todo item saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)