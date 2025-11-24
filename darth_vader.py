import requests

"""   Модуль для выполнения GET запроса с проверками: 
      - получаемый статус-код с ожидаемым 
      - наличие обязательных полей                      """
def get_url(url, expected_value):
    print(url)
    result_get = requests.get(url)
    print(result_get.status_code)

    """    Проверить получаемый статус-код с ожидаемым   """
    assert result_get.status_code == 200, 'ОШИБКА, Статус-код не совпадает'
    result_json = result_get.json()

    """    Проверить наличие обязательных полей   """
    assert list(result_json) == expected_value, 'ОШИБКА, Список полей не совпадает'
    print(result_json)

    return result_json


URL = " https://swapi.dev/api/people/4/"
NAME = "Darth Vader"
KEY_PEOPLE = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url']
KEY_FILM = ['title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'characters', 'planets', 'starships', 'vehicles', 'species', 'created', 'edited', 'url']

list_url_all_characters = []

"""   Получить список по герою   """
result_all = get_url(URL, KEY_PEOPLE)

"""    Проверить значение обязательного поля в ответе запроса   """
assert NAME == result_all.get("name"), 'ОШИБКА, Значение обязательного поля не совпадает'

"""    Получить список с url фильмов   """
url_films = result_all.get("films")
for url_film in url_films:
    result_film = get_url(url_film, KEY_FILM)

    """    Получить список c url персонажей   """
    url_characters = result_film.get("characters")
    list_url_all_characters += url_characters

"""    получить множество с url уникальных персонажей   """
unique_url_all_characters = set(list_url_all_characters)
list_unique_characters = []
for characters in unique_url_all_characters:
    result_characters = get_url(characters, KEY_PEOPLE)
    unique_characters = result_characters.get("name")

    """    Получить список персонажей   """
    list_unique_characters.append(unique_characters)

"""    Отсортировать список персонажей по алфавиту   """
list_unique_characters.sort()

"""    Количество персонажей   """
len_characters = len(list_unique_characters)

"""    Сохранить имена персонажей в файле 'characters.txt'   """
with open('characters.txt', 'w', encoding='UTF-8') as file:
    for i in range(len_characters):
        file.write(str(i+1).rjust(2, "0")+"/"+str(len_characters)+" : "+list_unique_characters[i]+"\n")

print(f"\nИмена всех персонажей, которые снимались в фильмах с {NAME} сохранены в файле 'characters.txt'")
