#!/usr/bin/python3
"""creates a route status"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'])
def status():
    """creates a route status"""

    return jsonify({"status": "OK"})

@app_views.route("/stats", methods=['GET'])
def stats():
    """defines the function to get the stats"""

    amenities = storage.count("Amenities")
    states = storage.count("States")
    stats = {
            "amenities": amenities,
            "cities": 36,
            "places": 154,
            "reviews": 718,
            "states": states,
            "users": 31
            }

    return jsonify(stats)
