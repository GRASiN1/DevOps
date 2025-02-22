from flask import Flask, request, render_template, jsonify
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["flaskTutorial"]
userCollection = db["users"]

app = Flask(__name__)

@app.route("/")
def Home():
    return "API running"

@app.route("/form", methods=["POST"])
def form():
    name = request.json.get("name")
    age = request.json.get("age")
    city = request.json.get("city") 
    userCollection.insert_one({"name": name, "age": age, "city": city})
    return f"Hello, {name}! you are {age} years old and you live in {city}"

@app.route("/users")
def users():
    users = userCollection.find()
    users = list(users)
    for user in users:
        user["_id"] = str(user["_id"])

    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")