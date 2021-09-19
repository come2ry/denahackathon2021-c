from app import common
from app import models
from typing import Optional
from app.common.geo import Geo as cGeo
from app.common.user import User as cUser
from app.common.locus import Locus as cLocus
from database import SessionLocal as session

# from sqlalchemy.orm import sessionmaker
# SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
# session = SessionClass()


def find_users_by_rectangle(top_left: cGeo, bottom_right: cGeo) -> list[cUser]:
    # 仮
    return [cUser(id=12, username="user_name_test", geo=cGeo(latitude=15.622, longitude=137.610))]
    # 地図上の長方形から含まれるユーザーを検索
    # TODO: geo長方形から含まれるlatlngを持つユーザーを検索したい
    musers = sessin.query(models.User()).all()
    cusers = [cUser.from_model(muser) for muser in musers]
    return cusers


def insert_geo_history(user_id: int, geo: cGeo) -> None:
    return  # 仮
    # User table へ 最新のlatlngを挿入
    muser = session.query(models.User(id=user_id)).one_or_none()
    muser.geo = geo  # TODO: 型をGeo->Geometry に変換する必要がある
    # Geo table へ 履歴として latlng を挿入
    # TODO: geoを型変換Geo->Geometryへ変換する必要がある
    session.add(models.Geo(user_id=user_id, latlng=geo))
    session.commit()


def insert_locus(user_id: int, locus: cLocus) -> int:
    return 20  # 仮
    # TODO: locusを変換?する必要がある
    mlocus = models.Locus(user_id=user_id, geos=locus)
    session.add(mlocus)
    session.commit()
    return mlocus.user_id


def find_locus(locus_id: int) -> cLocus:
    # 仮
    return cLocus(locus_id=53, user=cUser(id=35, username="seityo"), geos=[cGeo(latitude=15.622, longitude=137.610)])
    mlocus = session.query(models.Locus(id=locus_id)).first()
    return cLocus.from_model(mlocus)


def find_locus_by_victim(user_id: int) -> Optional[cLocus]:
    # 仮
    # return cLocus(locus_id=53, user=cUser(id=35, username="seityo"), geos=[cGeo(latitude=15.622, longitude=137.610)])
    mlocusnotify = session.query(models.LocusNotify).filter(
        models.LocusNotify.victim_user_id == user_id,
        models.LocusNotify.is_checked == False).one_or_none()
    if not mlocusnotify:
        return None

    mlocusnotify.is_checked = True
    session.commit()
    mlocus = session.query(models.Locus(id=mlocusnotify.locus_id)).first()
    return cLocus.from_model(mlocus)
