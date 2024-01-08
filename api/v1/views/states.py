#!/usr/bin/python3
""" object that handles all default RESTful API"""
from flask import jsonify, request, abort
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from models.state import State
import json


@app_views.route("/states", methods = ['POST', 'GET'])
def all_states():
    """defines a function to retrieve all the states creates a new state"""
    states = storage.all(State)
    if request.method == 'GET':
        state = [state.to_dict() for state in states.values()]
        return jsonify(state)


    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
        if 'name' not in data:
            abort(400, 'Missing name')
        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>")
def state_by_id(state_id):
    """returns state by Id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=['PUT', 'DELETE'])
def delete_update(state_id):
    """deletes or updates a state"""
    state = storage.get(State, state_id)
    if request.method == 'DELETE':
        if state is None:
            abort(404)
        else:
            storage.delete(state)
            storage.save()
            return {}, 200


    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            abort(404, 'Not a JSON')
        if 'name' not in data:
            abort(400, 'Missing name')


        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201

