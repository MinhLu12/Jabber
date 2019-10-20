from main.web_api_registrator import register_web_api_s
from main.configurations import Configuration as config

app = register_web_api_s()

if __name__ == '__main__':
    app.run(config.get("HOST"), config.get("PORT"))