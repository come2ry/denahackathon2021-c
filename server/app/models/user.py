from app.models import Base, datetime_jstnow
from database import db
from app.models.columntypes import Geometry

__all__ = ["User"]


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    latlng = db.Column(Geometry(2, 4326), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime_jstnow,
                           nullable=False)
    # google_id = Column(String(50), nullable=False)
