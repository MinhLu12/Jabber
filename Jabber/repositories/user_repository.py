from bson.json_util import dumps
from .database_singleton import db

def create_user(name, age):
    created_user = db().users.insert_one({ 'name': name, 'age': age })
    return dumps(created_user.inserted_id)

def get_users():
    return dumps(db().users.find_one({'name': 'minh'}))