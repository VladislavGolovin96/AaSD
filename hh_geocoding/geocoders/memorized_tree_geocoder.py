from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.dictionary = {}

        for country in self.__data:
            for area in country.areas:
                for city in area.areas:
                    self.dictionary[city.id] = f"{country.name} {area.name} {city.name}"
                self.dictionary[area.id] = f"{country.name} {area.name}"
            self.dictionary[country.id] = f"{country.name}"

    def _apply_geocoding(self, area_id: str) -> str:
        return self.dictionary.get(area_id, 'Что-то пошло не так!')

