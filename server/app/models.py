"""
DBのテーブルをPython Objectで定義
"""
import uuid

import utils
from datetime import datetime, timedelta, timezone

from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey,  # type: ignore
                        Index, Integer, SmallInteger, String, Table, Text,
                        UniqueConstraint, Boolean)
from sqlalchemy.orm import backref, relationship
from geoalchemy2 import Geometry  # type: ignore
from geoalchemy import GeometryColumn, Point
from geoalchemy.mysql import MySQLComparator
from database import Base
# from sqlalchemy import func
# from sqlalchemy.types import UserDefinedType


# class Geometry(UserDefinedType):
#     def get_col_spec(self):
#         return 'GEOMETRY'

#     def bind_expression(self, bindvalue):
#         return func.ST_GeomFromText(bindvalue, type_=self)

#     def column_expression(self, col):
#         return func.ST_AsText(col, type_=self)


# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')


# 引数は使っていないが，消してはいけない
def datetime_jstnow(time_zone=JST):
    return datetime.now(JST)


locus_geos_table = Table('locus_geos', Base.metadata,
                         Column('locus_id', Integer,
                                ForeignKey('locus.id')),
                         Column('geo_id', Integer,
                                ForeignKey('geo.id'))
                         )


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    latlng = Column(Geometry(geometry_type='POINT',
                    dimension=2, srid=4326), nullable=True)
    updated_at = Column(DateTime, default=datetime_jstnow,
                        index=True, nullable=False)
    # google_id = Column(String(50), nullable=False)


class Geo(Base):
    __tablename__ = 'geo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey('User.id'), nullable=False, index=True)
    latlng = Column(Geometry(geometry_type='POINT',
                    dimension=2, srid=4326), nullable=False)
    created_at = Column(DateTime, default=datetime_jstnow,
                        index=True, nullable=False)
    __table_args__ = (
        Index('latest_user_geo_idx', created_at.desc(), user_id, latlng),
    )

    user = relationship(
        'User',
        primaryjoin="User.id == Geo.user_id",
        backref=backref('geos',
                        uselist=True,
                        cascade='delete,all'),
        uselist=False,
    )


class Locus(Base):
    __tablename__ = 'locus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, primary_key=True, autoincrement=True)

    geos = relationship(
        'Geo',
        backref=backref('locus',
                        uselist=True,
                        cascade='delete,all'),
        uselist=False,
        secondary=locus_geos_table,
    )


class LocusNotify(Base):
    __tablename__ = 'locusNotify'
    id = Column(Integer, primary_key=True, autoincrement=True)
    locus_id = Column(
        Integer, ForeignKey('Locus.id'), nullable=False, index=True)
    victim_user_id = Column(
        Integer, ForeignKey('User.id'), nullable=False, index=True)
    is_checked = Column(SmallInteger, default=0, nullable=False)

    victim_user = relationship(
        'User',
        primaryjoin="User.id == LocusNotify.victim_user_id",
        backref=backref('locus_notify',
                        uselist=False,
                        cascade='delete,all'),
        uselist=False,
    )
