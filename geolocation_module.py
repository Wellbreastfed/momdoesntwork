from geopy.geocoders import Nominatim

class Geolocation:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="getLoc")

    def get_location_details(self, location_name):
        location = self.geolocator.geocode(location_name)
        return location
