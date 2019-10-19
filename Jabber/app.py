from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from repositories import user_repository

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r'/api/*': {"origins": "http://localhost:8080"}}, allow_headers='Content-Type')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class Users(Resource):
    def get(self):
        return user_repository.get_users()

    def post(self):
        return user_repository.create_user()

api.add_resource(Users, '/api/users')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, port = 5000)