from flask import Flask
from web_api_s.user_api import user_blueprint
from startup import configurations as config

def register_web_api_s():
    app = Flask(__name__)

    __register_user_api(app)

    return app

def __register_user_api(app):
    app.register_blueprint(
        user_blueprint,
        url_prefix="{prefix}/v{version}".format(
            prefix = config.get("URL_PREFIX"),
            version = config.get("API_VERSION")))