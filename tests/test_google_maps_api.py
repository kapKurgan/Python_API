import json
from ..utils.api import GoogleMapsApi



class Test_create_place():
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
