#!/usr/bin/python3
"""script starts a Flask web application"""
from flask import Flask, request

app_name = Flask(__name__)


@app_name.route("/", strict_slashes=False)
def home():
    """
    Route function for the home page.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


@app_name.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route function for '/hbnb' endpoint.

    Returns:
        str: A message indicating 'HBNB'.
    """
    return "HBNB"


@app_name.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route function for '/c/<text>' endpoint.

    Returns:
        str: A message indicating 'ctext'.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app_name.run(host='0.0.0.0', port=5000)
