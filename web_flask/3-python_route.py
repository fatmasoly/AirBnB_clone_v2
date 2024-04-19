#!/usr/bin/python3
"""script starts a Flask web application"""
from flask import Flask

app_name = Flask(__name__)


@app_name.route("/", strict_slashes=False)
def home():
    """ Route function for the home page"""
    return "Hello HBNB!"


@app_name.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route function for '/hbnb' endpoint"""
    return "HBNB"


@app_name.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route function for '/c/<text>' endpoint"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Route function for '/python/<text>' endpoint"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app_name.run(host='0.0.0.0', port=5000)
