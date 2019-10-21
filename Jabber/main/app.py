from main.web_api_registrator import register_web_api_s
from main.configurations import Configuration as config
from flask_cors import CORS

app = register_web_api_s()

CORS(app, resources={r'/api/*': {"origins": "http://localhost:8080"}}, allow_headers='Content-Type')

if __name__ == '__main__':
    app.run(config.get("HOST"), config.get("PORT"))