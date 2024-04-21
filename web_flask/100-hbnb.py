#!/usr/bin/python3
"""start Flask application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb')
def states():
    """display a HTML page"""
    states = storage.all("State", strict_slashes=False)
    amenities = storage.all("Amenity", strict_slashes=False)
    users = storage.all("User", strict_slashes=False)

    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           users=users)


@app.teardown_appcontext
def teardown_db(exception):
    """close db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
