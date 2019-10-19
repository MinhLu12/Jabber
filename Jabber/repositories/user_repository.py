from pymongo import *
from bson.json_util import *

client = MongoClient('mongodb://localhost:27017/')
mydb = client["test"]

posts = mydb.posts

def create_user():
    post_data = {
        'name': 'minh'
    }
    posts.insert_one(post_data)

def get_users():
    return dumps(posts.find_one({'name': 'minh'}))