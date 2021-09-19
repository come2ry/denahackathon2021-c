from sqlalchemy.types import UserDefinedType
from sqlalchemy import func
import os
from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from .geometry import *
from .geo import *
from .locus import *
from .user import *

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')


# 引数は使っていないが，消してはいけない


# class Geometry(UserDefinedType):
#     def get_col_spec(self):
#         return 'GEOMETRY'
#
#     def bind_expression(self, bindvalue):
#         return func.ST_GeomFromText(bindvalue, type_=self)
#
#     def column_expression(self, col):
#         return func.ST_AsText(col, type_=self)


def datetime_jstnow(time_zone=JST):
    return datetime.now(JST)


# engine = create_engine(
#     app.config["SQLALCHEMY_DATABASE_URI"],
#     **settings.app.config["SQLALCHEMY_ENGINE_OPTIONS"]
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ModelBase = declarative_base()
