#!/usr/bin/python3
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
my_dict = storage.all()

@app.teardown_appcontext
def teardown():
    storage.close()

@app.route("/states_list")
def states_list():
    return render_template('7-states_list.html', states_list=storage.all(State))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
