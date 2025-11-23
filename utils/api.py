from .http_methods import HttpMethods                        # импорт класса HttpMethods


BASE_URL = "https://rahulshettyacademy.com"     # Базовый адрес
KEY = "?key=qaclick123"
POST_RESOURCE = "/maps/api/place/add/json"      # ресурс метода POST
GET_RESOURCE = "/maps/api/place/get/json"       # ресурс метода Get
PUT_RESOURCE = "/maps/api/place/update/json"    # ресурс метода Put


class GoogleMapsApi():
    """Класс содержащий методы, для тестирования Google maps api"""

    @staticmethod
    def create_new_place():
        """Метод по созданию новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = BASE_URL + POST_RESOURCE + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)  # отправка метода POST, в котором указываем url и body
        print(result_post.json())
        print(result_post.status_code)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """   Метод для проверки новой локации   """

        get_url = BASE_URL + GET_RESOURCE + KEY + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения новой локации"""

        put_url = BASE_URL + PUT_RESOURCE + KEY
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.json())
        print(result_put.status_code)
        return result_put



