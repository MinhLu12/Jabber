from flask import Flask
from web_api_s import user_api, profile_api
from startup.configurations import Configuration as config

def register_web_api_s():
    app = Flask(__name__)
    
    __register_user_api(app)
    __register_profile_api(app)

    return app

def __register_user_api(app):
    app.register_blueprint(
        user_api.user_blueprint,
        url_prefix="{prefix}/v{version}".format(
            prefix = config.get("URL_PREFIX"),
            version = config.get("API_VERSION")))

def __register_profile_api(app):
    app.register_blueprint(
        profile_api.profile_blueprint,
        url_prefix="{prefix}/v{version}".format(
            prefix = config.get("URL_PREFIX"),
            version = config.get("API_VERSION")))