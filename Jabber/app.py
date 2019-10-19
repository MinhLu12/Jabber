from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS

from repositories import user_repository

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "http://localhost:8080"}}, allow_headers='Content-Type')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/api/users', methods = ['GET'])
def get_users():
    return user_repository.get_users()

@app.route('/api/users/', methods = ['POST'])
def create_user():
    user_repository.create_user()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, port = 5000)