import requests


class HttpMethods:
    """Класс по хранению HTTP методов"""

    headers = {'Content-type': 'application/json'}  # Заголовки проекта передавать в формате json
    cookie = ""                                     # Куки проекта

    @staticmethod   # сделать метод статичным, чтобы вызывать его откуда угодно
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
