from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from repositories import user_repository

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r'/api/*': {"origins": "http://localhost:8080"}}, allow_headers='Content-Type')

parser = reqparse.RequestParser()

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class UserCollection(Resource):
    def get(self):
        return user_repository.get_users()

api.add_resource(UserCollection, '/api/users')

class User(Resource):
    def post(self):
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('age', type = int, required = True)
        args = parser.parse_args()

        return user_repository.create_user(args['name'], args['age'])

api.add_resource(User, '/api/user')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, port = 5000)