#!/usr/bin/python3
"""This script defines the route of the app_views blueprint"""

from api.v1.views import app_views
from flask import jsonify
import models


@app_views.route('/status', strict_slashes=False)
def show_status():
    """This returns the status of the app"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def display_status():
    """This returns the status of each model"""
    model = models.storage
    res = {'amenities': model.count("Amenity"),
            'cities': model.count("City"),
            'places': model.count("Place"),
            'reviews': model.count("Review"),
            'states': model.count("State"),
            'users': model.count("User")}
    return jsonify(res)
