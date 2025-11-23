#  pytest -v -s tests\test_google_maps_api.py
import json

from ..utils.api import GoogleMapsApi
from ..utils.checking import Checking



class TestCreatePlace():
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("\n>>>>>>>>>>>>>   Метод POST   <<<<<<<<<<<<<<<<<<")
        result_post = GoogleMapsApi.create_new_place()          # вызов метода по созданию новой локации
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        check_post = result_post.json()
        place_id = check_post.get("place_id")                   # получения place_id для метода GET

        print(">>>>>>>>>>>>>   Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)      # отправка метода Get
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print(">>>>>>>>>>>>>   Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])

        print(">>>>>>>>>>>>>   Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print(">>>>>>>>>>>>>   Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        # token = result_delete.json()                             # получить все поля в json из ответа
        # print("token =", token)

        print(">>>>>>>>>>>>>   Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])


