from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Сделать перебор дерева для каждого area_id
            - В ходе перебора возвращать массив элементов, состоящих из TreeNode необходимой ветки
            - Из массива TreeNode составить полный адрес
        """
        # Проходим по всем странам
        for country in self.__data:
            # Если идентификатор совпадает с идентификатором страны
            if country.id == area_id:
                return country.name

            # Проходим по всем областям в стране
            for area in country.areas:
                # Если идентификатор совпадает с идентификатором области
                if area.id == area_id:
                    return f"{country.name} {area.name}"

                # Проходим по всем городам в области
                for city in area.areas:
                    # Если идентификатор совпадает с идентификатором города
                    if city.id == area_id:
                        return f"{country.name} {area.name} {city.name}"

        # Если ничего не найдено, возвращаем None
        return None


