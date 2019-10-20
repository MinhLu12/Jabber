from main.web_api_registrator import create_app
from main.configurations import Configuration as config

app = create_app()

if __name__ == '__main__':
    app.run(config.get("HOST"), config.get("PORT"))