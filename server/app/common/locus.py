from app.common.geo import Geo
from app.common.user import User
from typing import Optional
from sympy.geometry import Point, Polygon

class Locus:
    def __init__(self, locus_id:Optional[int], user:Optional[User], geos:list[Geo]):
        self.locus_id = locus_id
        self.geos = geos
        self.user = user
        self.datetime = None # TODO

    def dump(self):
        return {
            'locus_id': self.locus_id,
            'geos': self.geos,
            'user_id': self.user.id,
            'user_name': self.user.username,
            'datetime': self.datetime
        }

    def is_in(self, geo:Geo) -> bool:
        return Polygon(*self.geos).encloses_point(Point(geo['latitude'],geo['longitude']))

    def get_rectangle(self):
        latitudes = [geo['latitude'] for geo in self.geos]
        longitudes = [geo['longitude'] for geo in self.geos]
        left_top_geo = Geo(max(latitudes), min(longitudes))
        right_bottom_geo = Geo(min(latitudes), max(longitudes))
        return left_top_geo, right_bottom_geo