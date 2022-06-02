from crypt import methods
import json
from flask import Flask, jsonify, request

# creating an app
app = Flask(__name__)

# create an array of tasks with each task as a different object in it.
tasks = [
    {
        "id": 1,
        "contact" : 9999999999,
        "contact_of" : "Dad",
        "done": False,
    },
    {
        "id": 2,
        "contact" : 9898989898,
        "contact_of" : "Mom",
        "done": False,
    }
]


@app.route("/")
def hello_Soham():
    return "hello Soham"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "contact": request.json["contact"],
        "contact_of": request.json.get("contact_of", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })


if __name__ == "__main__":
    app.run(debug=True)
