# TODO: ここに共通処理をまとめる
from logger import logger
from . import datastore
import json
from app.common.geo import Geo
from app.common.locus import Locus
from app.common.user import User

def create_sample_user(user_data: dict) -> None:
    try:
        datastore.SAMPLE_USERS[len(datastore.SAMPLE_USERS) + 1] = user_data
        logger.info(f"<SampleUser {json.dumps(user_data)}>の作成処理 完了")
    except Exception as e:
        logger.error(f"<SampleUser {json.dumps(user_data)}>の作成処理 失敗")
        raise e

def get_user_geos(top_left:Geo, bottom_right:Geo) -> list[User]:
    try:
        return [User(12, "user_name_test", Geo(15.622, 137.610))]
        return db.find_geos_by_rectangle(top_left, bottom_right)
    except Exception as e:
        logger.error(f"<>...")
        raise e

def put_user_geo(user_id:int, geo:Geo) -> None:
    try:
        pass
        # db.insert_geo_history(user_id, geo)
    except Exception as e:
        logger.error(f"<>...")
        raise e

def put_user_locus(user_id:int, locus:list[dict]) -> int:
    try:
        return 15
        locus_id:int = db.insert_locus(user_id, locus)
        return locus_id
    except Exception as e:
        logger.error(f"<>...")
        raise e

def get_near_users(top_left:Geo, bottom_right:Geo) -> list[User]:
    try:
        return [User(12, "user_name_test", Geo(15.622, 137.610))]
        return db.find_users(top_left, bottom_right)
    except Exception as e:
        logger.error(f"<>...")
        raise e

def get_locus_by_id(locus_id:int) -> Locus:
    try:
        return Locus(locus_id=53, user=User(35, "seityo", None), geos=[Geo(15.622, 137.610)])
        return db.find_locus(locus_id)
    except Exception as e:
        logger.error(f"<>...")
        raise e

def get_locus_killed_me(user_id:int) -> Locus:
    try:
        return Locus(locus_id=53, user=User(35, "seityo", None), geos=[Geo(15.622, 137.610)])
        return db.find_locus_by_killed_user(user_id)
    except Exception as e:
        logger.error(f"<>...")
        raise e