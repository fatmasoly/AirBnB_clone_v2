#!/usr/bin/python3
"""ths is the first flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>')
def cities_by_states(id):
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    state_id = "State." + id

    if state_id in states.keys():
        return render_template("9-states.html",
                               state=states[state_id],
                               id=id)

    return render_template("9-states.html", not_found="not found")


@app.teardown_appcontext
def close_db(exception):
    """close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
