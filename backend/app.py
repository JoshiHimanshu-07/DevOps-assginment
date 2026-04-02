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

print(client.list_database_names())

# Flask app
app = Flask(__name__, template_folder='../frontend')

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

    result = collection.insert_one(data)

    return jsonify({
        "message": "Todo item saved successfully",
        "id": str(result.inserted_id)
    })

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0', port=7000)
    
    
    #fe07c53 (HEAD -> master_1) Added Item Hash field
#c7ca277 Added Item UUID field
#60a9bd Added Item ID field
=======
    app.run(debug=True, host='0.0.0.0', port=7000)
>>>>>>> ca2c54d005995ee1c1551b0e9062e93bd2509e86
