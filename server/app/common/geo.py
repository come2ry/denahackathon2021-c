class Geo:
    def __init__(self, *, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude

    def dump(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }