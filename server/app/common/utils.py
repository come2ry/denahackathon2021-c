# TODO: ここに共通処理をまとめる
from logger import logger
from . import datastore
import json


def create_sample_user(user_data: dict) -> None:
    try:
        datastore.SAMPLE_USERS[len(datastore.SAMPLE_USERS) + 1] = user_data
        logger.info(f"<SampleUser {json.dumps(user_data)}>の作成処理 完了")
    except Exception as e:
        logger.error(f"<SampleUser {json.dumps(user_data)}>の作成処理 失敗")
        raise e
