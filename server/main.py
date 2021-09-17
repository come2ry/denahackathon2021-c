import os
from pprint import pformat, pprint

# ユーザ定義
from app import create_app
from app.common import utils

# 環境変数`FLASK_ENV`を取得
env = os.environ.get('FLASK_ENV', 'development')  # default値は`development`
# config[env]のパスから設定を読み込んでappインスタンスを作成
app = create_app(env)

if __name__ == '__main__':
    # MEMO: loggingの方法
    from logger import logger
    logger.info(f"\nAPIルーティングマップ: \n{pformat(app.url_map)}\n")
    # logger.debug('DEBUG')
    # logger.info('INFO')
    # logger.warning('WARNING')
    # logger.error('ERROR')
    # logger.critical('CRITICAL')

    app.run(debug=True, host='0.0.0.0',
            port=os.environ.get('FLASK_RUN_PORT', 8080))
