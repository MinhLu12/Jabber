from flask import Flask, Blueprint
from flask_restful import Resource, Api
from repositories import user_repository as repository

blueprint = Blueprint('user_api', __name__)
api = Api(blueprint)

class UserCollection(Resource):
    def get(self):
        return repository.get_users()

api.add_resource(UserCollection, '/users')

class User(Resource):
    def post(self):
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('age', type = int, required = True)
        args = parser.parse_args()

        return repository.create_user(args['name'], args['age'])

api.add_resource(User, '/api/user')
