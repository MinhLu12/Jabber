from pymongo import *

def db():
    client = MongoClient('mongodb://localhost:27017/')
    return client["jabber"]