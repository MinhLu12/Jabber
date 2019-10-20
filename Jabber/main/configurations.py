import os

class Configuration:
    configurations = {
        "PORT": 5000,
        "HOST": os.environ.get('SERVER_HOST', 'localhost'),
        "URL_PREFIX": "/api",
        "API_VERSION": 1
    }

    @staticmethod
    def get(name):
        return Configuration.configurations[name]