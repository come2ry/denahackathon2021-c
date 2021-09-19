from app.common.geo import Geo
from app.common.user import User
from typing import Optional
from sympy.geometry import Point, Triangle, Polygon

class Locus:
    def __init__(self, *, geos:list[Geo], locus_id:Optional[int]=None, user:Optional[User]=None):
        self.locus_id = locus_id
        self.geos = geos
        self.user = user
        self.datetime = None # TODO

    def dump(self):
        return {
            'locus_id': self.locus_id,
            'geos': [geo.dump() for geo in self.geos],
            'user_id': self.user.id,
            'username': self.user.username,
            'datetime': self.datetime
        }

    def is_in(self, geo:Geo) -> bool:
        poly = Polygon(*[(geo.latitude, geo.longitude) for geo in self.geos])
        if not (isinstance(poly, Triangle) or isinstance(poly, Polygon)): return False
        return poly.encloses_point(Point(geo['latitude'],geo['longitude']))

    def get_rectangle(self):
        latitudes = [geo.latitude for geo in self.geos]
        longitudes = [geo.longitude for geo in self.geos]
        left_top_geo = Geo(max(latitudes), min(longitudes))
        right_bottom_geo = Geo(min(latitudes), max(longitudes))
        return left_top_geo, right_bottom_geo