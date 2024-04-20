#!/usr/bin/python3
"""script starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape

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


@app_name.route('/python', strict_slashes=False)
@app_name.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Route function for '/python/<text>' endpoint"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app_name.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route function for '/number/<n>' endpoint"""
    return "{} is a number".format(n)


@app_name.route('/number_template/<int:n>', strict_slashes=False)
def page_num(n):
    """Route function for '/number_template/<n>' endpoint"""
    return render_template('5-number.html', n=escape(n))


@app_name.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Route function for '/number_odd_or_even/<n>' endpoint"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app_name.run(host='0.0.0.0', port=5000)
