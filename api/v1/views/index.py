#!/usr/bin/python3
"""creates a route status"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.city import City
import json


@app_views.route("/status", methods=['GET'])
def status():
    """creates a route status"""

    return json.dumps({"status": "OK"}, indent=2)


@app_views.route("/stats", methods=['GET'])
def stats():
    """defines the function to get the stats"""

    stats = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    j_stats = json.dumps(stats, indent=2)

    return j_stats
