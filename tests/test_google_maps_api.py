import json
from ..utils.api import GoogleMapsApi



class TestCreatePlace():
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("\n>>>>>>>>>>>>>   Метод POST")
        result_post = GoogleMapsApi.create_new_place()          # вызов метода по созданию новой локации

        check_post = result_post.json()
        place_id = check_post.get("place_id")                   # получения place_id для метода GET

        print(">>>>>>>>>>>>>   Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)      # отправка метода Get