import os
# import codec


class BaseConfig(object):
    ENV = None
    Testing = False
    API_PREFIX = "/api/v1"
    JSON_AS_ASCII = False  # NOTE: これをしないとjsonifyの結果日本語が文字化けする


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = 'your secret key'
    DEBUG = True
    # env = os.environ.get('FLASK_ENV', 'development')  # default値は`development`
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset=utf8mb4".format(**{
        'user': 'root',
        'password': 'root_password',
        'port': 3306,
        'host': 'db',
        'name': 'test'
    })

    SQLALCHEMY_ECHO = True
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     "ssl_disabled": True
    # }

    print(
        f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{SQLALCHEMY_DATABASE_URI}")


class ProductionConfig(BaseConfig):
    ENV = 'production'
    SECRET_KEY = 'your secret key'


class TestConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    SECRET_KEY = 'your secret key'
    # TEST_SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1:3306/test_jobpacker?charset=utf8mb4"
