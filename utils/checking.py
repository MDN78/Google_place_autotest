"""Методы для проверки ответов запросов"""
import json


class Checking():
    """Метод для проверки статус кода"""
    @staticmethod  # тогда не нужен параметр self - тк мы не привязываемся ни к какому классу
    # два этапа - к какому методу обращаемся и какой ответ ожидаем
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Успешно! Статус код = {result.status_code}")
    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        # переведет ответ в формат json
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верен!")

    # метод чтобы обойти одиночные кавычки в теле ответа - проверим не весь ответ а только часть текста
    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Фраза {search_word} присутсвует!")