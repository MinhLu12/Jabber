from bson.json_util import dumps
from .database_singleton import db

def create_user():
    post_data = { 'name': 'minh' }
    db().users.insert_one(post_data)

def get_users():
    return dumps(db().users.find_one({'name': 'minh'}))