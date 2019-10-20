import os

class Configuration:
    configurations = {
        "PORT": 5000,
        "HOST": os.environ.get('SERVER_HOST', 'localhost')
    }

    @staticmethod
    def get(name):
        return Configuration.configurations[name]