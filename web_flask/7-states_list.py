#!/usr/bin/python3
"""ths is the first flask app"""
from flask import Flask, render_template
from models import storage
from models import *
from sqlalchemy import text


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display HTML page: (inside the tag BODY)"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda v: v.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(err=None):
    """close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
