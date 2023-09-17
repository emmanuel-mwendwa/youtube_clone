import os
import json

with open('youtube_config.json') as config_file:
    youtube_config = json.load(config_file)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = youtube_config.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}