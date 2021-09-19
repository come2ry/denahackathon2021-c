from app import common
from app import models
from typing import Optional

# from sqlalchemy.orm import sessionmaker
# SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
# session = SessionClass()

def find_users_by_rectangle(top_left:common.Geo, bottom_right:common.Geo) -> list[common.User]:
    return [common.User(user_id=12, username="user_name_test", geo=common.Geo(latitude=15.622, longitude=137.610))] # 仮
    # 地図上の長方形から含まれるユーザーを検索
    musers = sessin.query(models.User()).all() # TODO: geo長方形から含まれるlatlngを持つユーザーを検索したい
    cusers = [common.User.from_model(muser) for muser in musers]
    return cusers

def insert_geo_history(user_id:int, geo:common.Geo) -> None:
    return # 仮
    # User table へ 最新のlatlngを挿入
    muser = session.query(models.User(id=user_id)).get(1)
    muser.geo = geo # TODO: 型をGeo->Geometry に変換する必要がある
    # Geo table へ 履歴として latlng を挿入
    session.add(models.Geo(user_id=user_id, latlng=geo)) # TODO: geoを型変換Geo->Geometryへ変換する必要がある
    session.commit()

def insert_locus(user_id:int, locus:common.Locus) -> int:
    return 20 # 仮
    mlocus = models.Locus(user_id=user_id, geos=locus) # TODO: locusを変換?する必要がある
    session.add(mlocus)
    session.commit()
    return mlocus.user_id

def find_locus(locus_id:int) -> common.Locus:
    return common.Locus(locus_id=53, user=common.User(user_id=35, username="seityo"), geos=[common.Geo(latitude=15.622, longitude=137.610)]) # 仮
    mlocus = session.query(models.Locus(id=locus_id)).first()
    return common.Locus.from_model(mlocus)

def find_locus_by_victim(user_id:int) -> Optional[common.Locus]:
    return common.Locus(locus_id=53, user=common.User(user_id=35, username="seityo"), geos=[common.Geo(latitude=15.622, longitude=137.610)]) # 仮
    mlocusnotify = session.query(models.LocusNotify(victim_user_id=user_id, is_checked=False)).first()
    if not mlocusnotify: return None
    
    mlocusnotify.is_checked = True
    session.commit()
    mlocus = session.query(models.Locus(id=mlocusnotify.locus_id)).first()
    return common.Locus.from_model(mlocus)
