from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse
import datetime
from repositories import profile_repository as repository

profile_blueprint = Blueprint('profile_api', __name__)
profile_api = Api(profile_blueprint)

#class UserCollection(Resource):
#    def get(self):
#        return repository.get_users()

#profile_api.add_resource(UserCollection, '/users')

class Profile(Resource):
    def post(self):
        user = self.__get_passed_in_request()

        return repository.create(user)

    # user id
    # date made
    # limit_to_viewers
    # display name
    # holds all posts, microservices
    def __get_passed_in_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type = str, required = True)
        parser.add_argument('display_name', type = str, required = True)

        return parser.parse_args()

profile_api.add_resource(Profile, '/profile')
