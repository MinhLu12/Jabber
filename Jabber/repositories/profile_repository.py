from bson.json_util import dumps
from repositories.database_singleton import db

def create(profile):
    created_profile = db().profiles.insert_one(profile)
    return dumps(created_profile.inserted_id)