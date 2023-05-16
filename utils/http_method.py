# все методы GET PUT POST DELETE
import requests
"""Список HTTP методов"""
class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # @staticmethod - тогда не нужен параметр self - тк мы не привязываемся ни к какому классу
    @staticmethod # для того чтобы метод был статичен и мы могли вызывать его в других местах
    def get(url):
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result
