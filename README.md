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
3. импортируем в файл с нашими методами:<br/> 
```from utils.http_method import Http_method```
4. Создаем функции, согласно API документации, для:
    - создания новой локации<br/> ```def create_new_place():```
    - получения созданной локации<br/>```def get_new_place(place_id):```
    - изменение созданной локации<br/>```def put_new_place(place_id):```
    - удаления созданной локации<br/>```def delete_new_place(place_id):```
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
        place_id = check_post.get("place_id")
```
6. Методы необходимы следующие - сам запрос и его проверка, согласно документации API:
    - POST
    - GET => POST
    - PUT
    - GET => PUT
    - DELETE
    - GET => DELETE
7. Добавление Метода для проверки статус кода:
    - Создаем новый файл ```checking.py``` в котором будут созданы методы проверки статус кода
    - импортируем ``` import json```
    - создаем класс ```class Checking()```
    - создаем статичную функцию проверки статус кода<br/>
     ```
        @staticmethod
        def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Успешно! Статус код = {result.status_code}")
    ```
8. Добавление метода для проверки наличия обязательных полей
    - добавляем метод в файл ```checking```
    - создаем статичную функцию 
    ```     
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")
    ```

    - добавляем наш созданный метод, для этого в файл  ```test_google_maps_api``` добавляем в каждый наш метод  POST, GET, PUT, DELETE. В начале в первый метод POST:
    ```
    token = json.loads(result_post.text)
    print(list(token))
    Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    ``` 
    - 

