# Тестирование ПО: Автоматизация и Программирование.Python.API

## darth_vader.py - автоматизация поиска всех персонажей, которые снимались в фильмах с Дарт Вейдером

The Star Wars API https://swapi.dev/

Star Wars APIs & Explorer https://swapi.info/

Использование метода GET https://swapi.dev/api/people/4/, чтобы сохранять имена всех персонажей, которые снимались в фильмах с Дарт Вейдером, в файле 'characters.txt'

## Как запускать тесты и где смотреть логи

Чтобы запустить все тестовые файлы, используйте следующую команду:
```bash
pytest -v --tb=line 
```
или
```bash
pytest -v -s 
```

Чтобы запустить любой тестовый файл, перейдите в каталог с тестами (tests) и используйте следующую команду:
```bash
pytest -v --tb=line ИМЯ_ФАЙЛА.py
```

Чтобы посмотреть текстовый файл с логами, перейдите в каталог logs.

## Примечания
Если у вас возникли проблемы с запуском, попробуйте изменить пути импорта, версию pytest.
Загрузите все версии пакетов из файла requirements.txt, используйте следующую команду: 
```bash
pip install -r requirements.txt
```

# Добавлены отчеты Allure

## Как запускать тесты

Чтобы запустить тестовый файл, используйте следующую команду:

```bash
pytest -v -s --tb=line --alluredir=allure-results tests\test_google_maps_api.py
```

Отчет формируется в папке allure-results и запускается для просмотра командой:

```bash
allure serve allure-results
```

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_1.png)

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_2.png)

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_3.png)

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_4.png)

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_5.png)

![alt tag](https://github.com/kapKurgan/Python_API/blob/main/github_pict/allure_api_6.png)
