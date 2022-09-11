#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask, request, render_template
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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Routes '/states_list' to a template-based html page using a database"""
    return render_template('7-states_list.html',
                           states_list=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
