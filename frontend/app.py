from flask import Flask, render_template, request, jsonify
import requests

BACKEND_URL = "http://0.0.0.0:5000"

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form():
    formData = dict(request.form)
    response = requests.post(f"{BACKEND_URL}/form", json=formData)
    return response.text

@app.route("/getUsers")
def getUsers():
    response = requests.get(f"{BACKEND_URL}/users")
    return response.json()

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")