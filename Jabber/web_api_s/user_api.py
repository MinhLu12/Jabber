from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse
from repositories import user_repository as repository

user_blueprint = Blueprint('user_api', __name__)
user_api = Api(user_blueprint)

class UserCollection(Resource):
    def get(self):
        return repository.get_users()

user_api.add_resource(UserCollection, '/users')

class User(Resource):
    def post(self):
        user = self.__get_passed_in_request()

        return repository.create(user)

    def __get_passed_in_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('age', type = int, required = True)

        return parser.parse_args()

user_api.add_resource(User, '/user')
