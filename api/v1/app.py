#!/usr/bin/python3
"""The script creates of a REST API"""

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_app(exc):
    """This method closes the app """
    storage.close()


@app.errorhandler(404)
def error_handler(e):
    """This returns a 404 page"""
    data = {"error": "Not found"}
    return jsonify(data), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
