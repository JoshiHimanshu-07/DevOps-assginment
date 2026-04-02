import os
from flask import Flask, render_template, request, jsonify
from flask.cli import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv("client")
client = MongoClient(mongo_uri)

db = client["todoDB"]
collection = db["todoItems"]

# Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def form():
    return render_template('todo.html')

# Submit route
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return jsonify({
        "message": "Todo item saved successfully",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)