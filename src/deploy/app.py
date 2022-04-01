"""Demo to try out Flask
"""
from pathlib import Path

from flask import Flask, jsonify, request
from src.models.model import MyModel

app = Flask(__name__)
# TODO: Make model parameters changeable via requests
model = MyModel(Path("../models/parameters.yaml"))


@ app.route("/")
def hello_world() -> str:
    """hello world

    Returns:
        str: Hello World!
    """
    return "<p>Hello, World!</p>"


@app.route("/prediction_api", methods=["POST"])
def predict():
    """Do a prediction on the received request

    Returns:
        _type_: _description_
    """
    data = request.get_json(force=True)  # type: ignore  Pylance cannot resolve the LocalProxy properly
    if data is not None:
        prediction = model.provide_prediction(data["input"])
    else:
        prediction = "Could not parse request!"
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
