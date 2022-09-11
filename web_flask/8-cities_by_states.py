#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """Called on exit"""
    storage.close()


@app.route("/cities_by_states")
def cities_by_state():
    """Routes '/cities_by_states' to a template-based html using a database"""
    return render_template('8-cities_by_states.html',
                           states_list=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
