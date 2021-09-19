# from app.models import datetime_jstnow
from database import db, Base
from app.models.columntypes import Geometry
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')


def datetime_jstnow(time_zone=JST):
    return datetime.now(JST)


__all__ = ["User"]


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    latlng = db.Column(Geometry(2, 4326), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime_jstnow,
                           nullable=False)
    # google_id = Column(String(50), nullable=False)
