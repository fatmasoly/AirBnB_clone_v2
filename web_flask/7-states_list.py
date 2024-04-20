#!/usr/bin/python3
"""script starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def state_list():
    """display a HTML page with the states list"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda v: v.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_DB(exception):
    """close the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.route.run(host="0.0.0.0", port=5000)
