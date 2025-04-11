import flask
import json
import os
from pymongo import MongoClient
from flask import request, render_template, redirect, url_for, flash

app = flask.Flask(__name__)
app.secret_key = 'w27faw9g84ag1ww2fawf14fa54!@#$%^&*'

client = MongoClient(
    "mongodb+srv://devops:easy@cluster0.napjccr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tls=True
)
db = client['Devops']
collection = db['assignment']

@app.route("/api")
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return flask.jsonify(data)
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    try:
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'message': request.form.get('message')
        }
        collection.insert_one(data)
        return redirect(url_for('success'))
    except Exception as e:
        flash(f"Error: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")