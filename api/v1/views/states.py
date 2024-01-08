#!/usr/bin/python3
""" object that handles all default RESTful API"""
from flask import jsonify, request, abort
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from models.state import State
import json


@app_views.route("/states")
def all_states():
    """defines a function to retrieve all the states"""
    states = storage.all(State)
    state = [state.to_dict() for state in states.values()]

    return jsonify(state)


@app_views.route("/states/<state_id>")
def state_by_id(state_id):
    """returns state by Id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify(state.to_dict())
