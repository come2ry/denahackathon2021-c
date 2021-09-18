from app.common.geo import Geo

class User:
    def __init__(self, id:int, username:str, geo:Geo):
        self.id = id
        self.username = username
        self.geo = geo

    def dump(self):
        return {
            'id': self.id,
            'username': self.username,
            'latitude': self.geo["latitude"],
            'longitude': self.geo["longitude"]
        }