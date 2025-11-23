import json

import requests

class AnswersToTask():
    """   Класс содержащий методы, для тестирования заданий по api   """

# https://stepik.org/lesson/846652/step/1?unit=850404
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

# https://stepik.org/lesson/846653/step/1?unit=850405
    @staticmethod
    def create_test_8_3_3():
        headers = { "x-api-key": "reqres-free-v1" }
        url = "https://reqres.in/api/users/2"
        print("\n#################### create_test_8_3_3")
        print(url)
        result_get = requests.get(url, headers=headers)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    @staticmethod
    def create_test_8_3_4():
        headers = { "x-api-key": "reqres-free-v1" }
        url = "https://reqres.in/api/users?page=2"
        print("\n#################### create_test_8_3_4")
        print(url)
        result_get = requests.get(url, headers=headers)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    @staticmethod
    def create_test_8_3_5():
        headers = { "x-api-key": "reqres-free-v1" }
        url = "https://reqres.in/api/users/15"
        print("\n#################### create_test_8_3_5")
        print(url)
        result_get = requests.get(url, headers=headers)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    @staticmethod
    def create_test_8_3_6():
        headers = { "x-api-key": "reqres-free-v1" }
        url = "https://reqres.in/api/unknown/2"
        print("\n#################### create_test_8_3_6")
        print(url)
        result_get = requests.get(url, headers=headers)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

# https://stepik.org/lesson/846654/step/1?unit=850406
    @staticmethod
    def create_test_8_5_3():
        json_put = [
            {
                "id": 1,
                "category": {
                    "id": 1,
                    "name": "Bobik"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": "1",
                        "name": "Bob"
                    }
                ],
                "status": "available"
            }
        ]
        url = "https://petstore.swagger.io/v2/pet"
        print("\n#################### create_test_8_5_3")
        print(url)
        result_put = requests.put(url, json=json_put)
        print(result_put.json())
        print(result_put.status_code)
        return result_put

    @staticmethod
    def create_test_8_5_4():
        headers = {
            "x-api-key": "reqres-free-v1"
        }

        json_put = [
            {
                "name": "morpheus",
                "job": "zion resident"
            }
        ]
        url = "https://reqres.in/api/users/3"
        print("\n#################### create_test_8_5_4")
        print(url)
        result_put = requests.put(url, json=json_put, headers=headers)
        print(result_put.json())
        print(result_put.status_code)
        return result_put

# https://stepik.org/lesson/846657/step/1?unit=850409
    @staticmethod
    def create_test_8_6_3():
        url = "https://petstore.swagger.io/v2/store/order/1"
        print("\n#################### create_test_8_6_3")
        print(url)
        result_delete = requests.delete(url)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete

    @staticmethod
    def create_test_8_6_4():
        url = "https://reqres.in/api/users/2"
        headers = {"x-api-key": "reqres-free-v1"}
        print("\n#################### create_test_8_6_4")
        print(url)
        result_delete = requests.delete(url, headers=headers)
#        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete

    @staticmethod
    def create_test_8_8_3():
        url = "https://catfact.ninja/fact?max_length=100"
        print("\n#################### create_test_8_8_3")
        print(url)
        result_get = requests.get(url)
        print(result_get.json())
        print(result_get.status_code)
        fields = json.loads(result_get.text)
        print(list(fields))
        return result_get

    @staticmethod
    def create_test_8_8_4():
        url = "https://catfact.ninja/facts?max_length=100&limit=5"
        print("\n#################### create_test_8_8_4")
        print(url)
        result_get = requests.get(url)
        print(result_get.json())
        print(result_get.status_code)
        fields = json.loads(result_get.text)
        print("=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=",list(fields))
        return result_get
