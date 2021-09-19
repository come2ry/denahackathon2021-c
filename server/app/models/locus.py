from app.models import db, Base, datetime_jstnow
from sqlalchemy.orm import backref, relationship

locus_geos_table = db.Table('locus_geos', Base.metadata,
                            db.Column('locus_id', db.Integer,
                                      db.ForeignKey('locus.id')),
                            db.Column('geo_id', db.Integer,
                                      db.ForeignKey('geo.id'))
                            )


class Locus(Base):
    __tablename__ = 'locus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('User.id'), nullable=False, index=True)

    geos = relationship(
        'Geo',
        backref=backref('locus',
                        uselist=True,
                        cascade='delete,all'),
        uselist=False,
        secondary=locus_geos_table,
    )

    user = relationship(
        'User',
        primaryjoin="User.id == Locus.user_id",
        backref=backref('locus',
                        uselist=False,
                        cascade='delete,all'),
        uselist=False,
    )

class LocusNotify(Base):
    __tablename__ = 'locusNotify'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    locus_id = db.Column(
        db.Integer, db.ForeignKey('Locus.id'), nullable=False, index=True)
    victim_user_id = db.Column(
        db.Integer, db.ForeignKey('User.id'), nullable=False, index=True)
    is_checked = db.Column(db.SmallInteger, default=0, nullable=False)

    victim_user = relationship(
        'User',
        primaryjoin="User.id == LocusNotify.victim_user_id",
        backref=backref('locus_notify',
                        uselist=False,
                        cascade='delete,all'),
        uselist=False,
    )

    locus = relationship(
        'Locus',
        primaryjoin="Locus.id == LocusNotify.locus_id",
        backref=backref('locus_notifies',
                        uselist=True,
                        cascade='delete,all'),
        uselist=False,
    )
