#!/usr/bin/python3
""" object that handles all default RESTful API"""

from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage


@app_views.route("/states")
def all_states():
    """defines a function to retrieve all the states"""
    states = storage.all(States)
    print(states)
    return states
