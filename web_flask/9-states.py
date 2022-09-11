#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """list all states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """list a specific state with their cities"""
    states = storage.all(State).values()
    state = None
    for stat in states:
        if (stat.id == id):
            state = stat
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
