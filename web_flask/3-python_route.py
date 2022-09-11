#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Routes '/' to generic html"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Routes '/hbnb' to generic html"""
    return "HBNB"


@app.route("/c/<text>")
def ctext(text=None):
    """Routes '/c/<text>' to generic html"""
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """Routes '/python/<text>' to generic html"""
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
