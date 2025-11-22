import requests


class Http_methods:
    """Класс по хранению HTTP методов"""

    headers = {'Content-type': 'application/json'}  # Заголовки проекта передавать в формате json
    cookie = ""                                     # Куки проекта

    @staticmethod   # сделать метод статичным, чтобы вызывать откуда угодно
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result
