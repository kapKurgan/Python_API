import requests
from ..utils.logger import Logger

class HttpMethods:
    """Класс по хранению HTTP методов"""

    headers = {'Content-type': 'application/json'}  # Заголовки проекта передавать в формате json
    cookie = ""                                     # Куки проекта

    @staticmethod   # сделать метод статичным, чтобы вызывать его откуда угодно
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
