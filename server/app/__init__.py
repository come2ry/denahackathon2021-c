import logging
import coloredlogs
from flask import Flask
from flask_cors import CORS
# TODO: 以降`server/app/resources/*.py`で定義したBluePrintをここでimportしていく
from app.resources import sample, geo, locus

# `FLASK_ENV`にConfigクラスをマッピング
config = {
    'development': 'config.DevelopmentConfig',
    'production': 'config.ProductionConfig',
    'test': 'config.TestConfig',
}


def create_app(flask_env: str):
    app = Flask(__name__)
    app.config.from_object(config[flask_env])
    CORS(app)

    # TODO: 以降`server/app/resources/*.py`で定義したBluePrintをここで登録していく
    # app.register_blueprint(sample.api_bp, url_prefix=app.config["API_PREFIX"])
    app.register_blueprint(geo.api_bp, url_prefix=app.config["API_PREFIX"])
    app.register_blueprint(locus.api_bp, url_prefix=app.config["API_PREFIX"])

    return app


app = create_app("test")
