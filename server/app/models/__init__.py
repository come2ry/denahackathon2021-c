from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta


# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

# 引数は使っていないが，消してはいけない


def datetime_jstnow(time_zone=JST):
    return datetime.now(JST)


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime_jstnow()
        self.updated_at = self.created_at
