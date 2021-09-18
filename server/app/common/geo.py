class Geo:
    def __init__(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_latlng(latlng):
        return Geo(latlng["lat"], latlng["lng"])