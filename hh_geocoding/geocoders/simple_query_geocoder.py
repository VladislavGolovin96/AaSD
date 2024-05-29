from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:

        node = API.get_area(area_id)
        address = node.name

        if node.parent_id is None:
            return address
        while node := API.get_area(node.parent_id):

            address = node.name + ' || ' + address

            if node.parent_id is None:
                break

            return address
