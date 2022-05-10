from flask import Flask, request, jsonify
from itsdangerous import json


app = Flask(__name__)

@app.route("/todolist")
def todo():
    return jsonify({"Msg": "Hello world from API"})

if __name__ == "__main__":
    app.run(debug=True)