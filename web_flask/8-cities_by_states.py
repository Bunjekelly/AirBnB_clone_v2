#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """print all the cities in the database"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(ctx):
    """Remove the current SQL Alchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
