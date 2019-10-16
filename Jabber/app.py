from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder = './client/templates')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    client = MongoClient('mongodb://localhost:27017/');
    mydb = client["test"];

    posts = mydb.posts;
    
    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data);

    name = posts.find_one({'author': 'Scott'});

    return render_template('index.html', name = name);

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)