# Google_place_autotest
## Построение проекта автоматизации проверки API

### Шаг 1. Создание кастомных метдов
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
6. Создаем функции отвечающие за конкретные запросы(GET, POST, PUT, DELETE) в формате:
```
    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result
```

$ git jd
```