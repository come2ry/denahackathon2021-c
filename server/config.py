import os


class BaseConfig(object):
    ENV = None
    Testing = False
    API_PREFIX = "/api/v1"
    JSON_AS_ASCII = False  # NOTE: これをしないとjsonifyの結果日本語が文字化けする


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = 'your secret key'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    #     'user': 'test',
    #     'password': 'test',
    #     'host': 'db',
    #     'name': 'db.postgresql'
    # })
    # SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@/prod_jobpacker?unix_socket=/Applications/MAMP/tmp/mysql/mysql.sock&charset=utf8"
    # env = os.environ.get('FLASK_ENV', 'development')  # default値は`development`
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}=@{host}:{port}/{name}?charset=utf8mb4".format(**{
        'user': 'root',
        'password': 'root_password',
        'port': 13306,
        'host': '127.0.0.1',
        'name': 'test'
    })


class ProductionConfig(BaseConfig):
    ENV = 'production'
    SECRET_KEY = 'your secret key'


class TestConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    SECRET_KEY = 'your secret key'
    # TEST_SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1:3306/test_jobpacker?charset=utf8mb4"
