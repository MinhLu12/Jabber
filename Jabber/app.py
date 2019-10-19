from flask import *
from pymongo import *
from bson.json_util import *
from flask_cors import *

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "http://localhost:8080"}}, allow_headers='Content-Type')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/api/users', methods = ["GET"])
def get_users():
    client = MongoClient('mongodb://localhost:27017/')
    mydb = client["test"]

    posts = mydb.posts
    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data)

    name = posts.find_one({'author': 'Scott'})

    return dumps(name)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, port = 5000)