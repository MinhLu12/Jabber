from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/test', methods = ["GET"])
def hello():
    client = MongoClient('mongodb://localhost:27017/');
    mydb = client["test"];

    posts = mydb.posts;
    
    #post_data = {
    #    'title': 'Python and MongoDB',
    #    'content': 'PyMongo is fun, you guys',
    #    'author': 'Scott'
    #}
    #result = posts.insert_one(post_data);

    name = posts.find_one({'author': 'Scott'});

    return dumps(name);

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)