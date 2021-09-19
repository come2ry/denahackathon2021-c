import os
from datetime import datetime, timedelta, timezone
from database import Base as ModelBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

# 引数は使っていないが，消してはいけない


def datetime_jstnow(time_zone=JST):
    return datetime.now(JST)


db = SQLAlchemy()

# engine = create_engine(
#     app.config["SQLALCHEMY_DATABASE_URI"],
#     **settings.app.config["SQLALCHEMY_ENGINE_OPTIONS"]
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ModelBase = declarative_base()


class Base(ModelBase):
    __abstract__ = True
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime_jstnow()
        self.updated_at = self.created_at