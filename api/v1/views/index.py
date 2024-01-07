#!/usr/bin/python3
"""creates a route status"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'])
def status():
    """creates a route status"""

    return jsonify({"status": "OK"})
