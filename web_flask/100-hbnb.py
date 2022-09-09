#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/hbnb")
def states():
    """Routes '/hbnb' to a template-based html using a database"""
    return render_template('100-hbnb.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
