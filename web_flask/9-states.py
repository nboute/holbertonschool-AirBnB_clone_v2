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


@app.route("/states")
def states():
    """Routes '/states' to a template-based html using a database"""
    return render_template('9-states.html',
                           states=storage.all(State))


@app.route("/states/<id>")
def states_by_id(id):
    """Routes '/states/<id>' to a template-based html using a database"""
    state = storage.all(State).get('State.{}'.format(id))
    return render_template('9-states.html',
                           state=storage.all(State).get('State.{}'.format(id)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
