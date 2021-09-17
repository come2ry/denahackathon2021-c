import os


class BaseConfig(object):
    ENV = None
    Testing = False
    API_PREFIX = "/api/v1"
    JSON_AS_ASCII = False  # NOTE: これをしないとjsonifyの結果日本語が文字化けする


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = 'your secret key'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    SECRET_KEY = 'your secret key'


class TestConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    SECRET_KEY = 'your secret key'
