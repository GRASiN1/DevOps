from flask import Flask, jsonify
from bussiness import get_Data

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api", methods=["GET"])
def api():
    data = get_Data()
    data = {"data": data}
    return jsonify(data)
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)