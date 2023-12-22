#!/usr/bin/python3
"""run the web app with Flask"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a html page with from web static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
