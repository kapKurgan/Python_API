import requests

class AnswersToTask():
    """   Класс содержащий методы, для тестирования заданий по api   """

    @staticmethod
    def create_test_8_2_9():
        headers = {
            "x-api-key": "reqres-free-v1"}
        json_post = {
            "name": "morpheus",
            "job": "leader"}
        url = "https://reqres.in/api/users"
        print("\n#################### create_test_8_2_9")
        print(url)
        result_post = requests.post(url, json=json_post, headers=headers)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def create_test_8_2_10():
        headers = {
            "x-api-key": "reqres-free-v1"}
        json_post = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"}
        url = "https://reqres.in/api/register"
        print("\n#################### create_test_8_2_10")
        print(url)
        result_post = requests.post(url, json=json_post, headers=headers)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def create_test_8_2_11():
        headers = {
            "x-api-key": "reqres-free-v1"}
        json_post = [
            {
                "id": 1,
                "username": "string",
                "firstName": "string",
                "lastName": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
        url = "https://petstore.swagger.io/v2/user/createWithArray"
        print("\n#################### create_test_8_2_11")
        print(url)
        result_post = requests.post(url, json=json_post, headers=headers)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def create_test_8_2_12():
        headers = {
            "x-api-key": "reqres-free-v1"}
        json_post = [{
                "username": "1",
                "email": "1@mail.ru",
                "password": "qwer1234"}]
        url = "https://reqres.in/api/login"
        print("\n#################### create_test_8_2_12")
        print(url)
        result_post = requests.post(url, json=json_post, headers=headers)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def create_test_8_2_13():
        headers = {
            "x-api-key": "reqres-free-v1"}
        json_post = [{
                "email": "peter@klaven"}]
        url = "https://reqres.in/api/login"
        print("\n#################### create_test_8_2_13")
        print(url)
        result_post = requests.post(url, json=json_post, headers=headers)
        print(result_post.json())
        print(result_post.status_code)
        return result_post
