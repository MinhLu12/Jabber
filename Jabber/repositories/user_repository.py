from bson.json_util import dumps
from repositories.database_singleton import db

def create(user):
    created_user = db().users.insert_one(user)
    return dumps(created_user.inserted_id)

def get_users():
    all_users = list(db().users.find())
    return dumps(all_users)