from flask import Flask
import flask_restful
import os

from v1 import api_v1_bp

def create_app(environment=None):
    app = Flask(__name__)

    app.register_blueprint(
        api_v1_bp,
        url_prefix='/api/v1')

    return app