#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close(exception):
    """Called on exit"""
    storage.close()


@app.route("/states")
def states():
    """Routes '/states' to a template-based html using a database"""
    return render_template('9-states.html',
                           states=storage.all(State).values())


@app.route("/states/<id>")
def states_by_id(id):
    """Routes '/states/<id>' to a template-based html using a database"""
    states = storage.all(State).values()
    state = None
    for elem in states:
        if id == elem.id:
            state = elem
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
