#!/usr/bin/python3
"""This module starts a Flask web application:"""
from flask import Flask, abort, render_template

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
def text(text=None):
    """Routes '/c/<text>' to generic html"""
    return f'C {text.replace("_", " ")}'


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """Routes '/python/<text>' to generic html"""
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<n>")
def number(n):
    """Routes '/number/<n>' to generic html if number is an integer"""
    try:
        return f'{int(n)} is a number'
    except ValueError as e:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """Routes '/number_template/<n>' to a html page made from a template"""
    try:
        return render_template('5-number.html', n=int(n))
    except ValueError as e:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
