from .http_methods import HttpMethods                        # импорт класса HttpMethods

BASE_URL = "https://rahulshettyacademy.com"
KEY = "?key=qaclick123"


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

        POST_RESOURCE = "/maps/api/place/add/json"  # ресурс метода POST
        post_url = BASE_URL + POST_RESOURCE + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)  # отправка метода POST, в котором указываем url и body
        print(result_post.json())
        print(result_post.status_code)
        return result_post


