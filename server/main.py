import os
from pprint import pformat, pprint

# ユーザ定義
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from app.common import utils

# 環境変数`FLASK_ENV`を取得
env = os.environ.get('FLASK_ENV', 'development')  # default値は`development`
# config[env]のパスから設定を読み込んでappインスタンスを作成
app = create_app(env)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    host='0.0.0.0', port=os.environ.get('FLASK_RUN_PORT', 8080)))


@app.cli.command('createdb')
def create_db():
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    print(database_exists(engine.url))


if __name__ == '__main__':
    # MEMO: loggingの方法
    from logger import logger
    logger.info(f"\nAPIルーティングマップ: \n{pformat(app.url_map)}\n")
    # logger.debug('DEBUG')
    # logger.info('INFO')
    # logger.warning('WARNING')
    # logger.error('ERROR')
    # logger.critical('CRITICAL')

    manager.run()
