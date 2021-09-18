from app.models import db, Base, datetime_jstnow


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    latlng = db.Column(db.Geometry(geometry_type='POINT',
                                   dimension=2, srid=4326), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime_jstnow,
                           index=True, nullable=False)
    # google_id = Column(String(50), nullable=False)
