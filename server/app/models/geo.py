from app.models import Base, datetime_jstnow
from database import db, Base
# from geoalchemy2 import Geometry  # type: ignore
from sqlalchemy.orm import backref, relationship
from app.models.columntypes import Geometry

__all__ = ["Geo"]


class Geo(Base):
    __tablename__ = 'geo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('User.id'), nullable=False, index=True)
    latlng = db.Column(Geometry(2, 4326), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime_jstnow,
                           index=True, nullable=False)
    __table_args__ = (
        db.Index('user_geo_idx', created_at.desc(), user_id),
        # db.Index('latest_user_geo_idx', created_at.desc(), user_id, latlng),
    )

    user = relationship(
        'User',
        primaryjoin="User.id == Geo.user_id",
        backref=backref('geos',
                        uselist=True,
                        cascade='delete,all'),
        uselist=False,
    )
