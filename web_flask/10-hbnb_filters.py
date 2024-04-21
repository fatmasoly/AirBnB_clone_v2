#!/usr/bin/python3
"""start Flask application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters')
def states():
    """display a HTML page"""
    states = storage.all("State", strict_slashes=False)
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """close db"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
