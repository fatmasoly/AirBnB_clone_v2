#!/usr/bin/python3
"""ths is the first flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    """Display HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(exception):
    """close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
