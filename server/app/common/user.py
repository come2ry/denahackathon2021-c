from app.common.geo import Geo
from typing import Optional
from app.models.user import User as mUser

class User:
    def __init__(self, *, id:int, username:Optional[str]=None, geo:Optional[Geo]=None):
        self.id = id
        self.username = username
        self.geo = geo

    def dump(self):
        return {
            'id': self.id,
            'username': self.username,
            'latitude': self.geo.latitude,
            'longitude': self.geo.longitude
        }

    @staticmethod
    def from_model(muser: mUser):
        geo = Geo(latitude=muser.latlng['lat'], longitude=muser.latlng['lng'])
        return User(id=muser.id, username=muser.username, geo=geo)