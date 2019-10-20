from flask import Flask

from web_api_s.user_api import api_v1_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        api_v1_bp,
        url_prefix='/api/v1')

    return app