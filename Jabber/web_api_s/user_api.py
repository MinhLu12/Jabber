from flask import Flask, Blueprint
import flask_restful


api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = flask_restful.Api(api_v1_bp)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
            'hello': 'world',
            'version': 1,
            }


api_v1.add_resource(HelloWorld, '/helloworld')