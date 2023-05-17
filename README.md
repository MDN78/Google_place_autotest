# Google_place_autotest
## Построение проекта автоматизации проверки API
- сайт проекта: https://rahulshettyacademy.com
- ключ: "?key=qaclick123"


### Шаг 1. Создание списка кастомных метдов
1. Создаем проект  ```apiProject```
2. Создаем папки:
    - ```tests```
    - ```utils```
3. В папке ```utils``` создаем файл ```http_methods.py``` где будут созданы запросы.
4. В файле ```http_methods``` создаем кастомные методы проверки запросов (GET, POST, PUT, DELETE).
5. Создаем класс ```Http_method```
```
import requests

class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
```
6. Создаем функции отвечающие за конкретные запросы(GET, POST, PUT, DELETE) в формате:<br/>
**Метод GET**
```
    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result
```
**Остальные методы**
```
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result
```
### Шаг 2. Создание методов для тестирования API

1. Создаем файл ```api.py```
2. Создаем класс ```class Google_maps_api():```
3. импортируем в файл с методами:<br/> 
```from utils.http_method import Http_method```
4. Создаем функции для:
- создания новой локации
- получения созданной локации
- изменение созданной локации
- удаления созданной локации
```
    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
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
        post_resource = "/maps/api/place/add/json"                  
        post_url = base_url + post_resource + key
        print(post_url)                                             
        result_post = Http_method.post(post_url, json_for_create_new_place)   
        print(result_post.text)
        return result_post
```
### Шаг 3. Создание тестов

1. В папке ```tests``` создать файл ```test_google_maps_api.py```
2. Слово ```test``` обязательно в названии файла теста - по нему pytest запускае тесты
3. импортируем в данный файл из файла api наш класс Google maps:<br/>
```from utils.api import Google_maps_api```
4. Создаем класс, где будем хранить все методы тестирования:<br/>
```class Test_create_place():```
5. Создаем методы в формате:

```
    def test_create_new_place(self):
        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
```
6. Методы необходимы следующие - сам запрос и его проверка:
    - POST
    - GET => POST
    - PUT
    - GET => PUT
    - DELETE
    - GET => DELETE
