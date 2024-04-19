#!/usr/bin/python3
"""script starts a Flask web application"""
from flask import Flask

app_name = Flask(__name__)


@app_name.route("/", strict_slashes=False)
def home():
    """
    Route function for the home page.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app_name.run(host='0.0.0.0', port=5000)
