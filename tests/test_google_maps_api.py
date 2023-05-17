# первым шагом импортируем наш метод с файла api наш класс который будем тестировать
from utils.api import Google_maps_api
from utils.checking import Checking
import json
import allure
"""Тесты - Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class Test_create_place():
    @allure.description("Test create, update, delete new location")
    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id") # чтобы система вернула нам номер place id который мы получим с json
        Checking.check_status_code(result_post, 200)
        # чтобы не переписывать все ключи из ответа json как в примере PUT
        # - делаем так: выведется список и его скопируем уже в checking
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # вызываем метод проверки значений обязательных полей
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\nМетод GET => POST")
        result_get = Google_maps_api.get_new_place(place_id)    # сюда передаем place id  с предыдущей функции
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number',
                                               'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("\nМетод PUT")
        result_put = Google_maps_api.put_new_place(place_id)    # сюда передаем place id  с предыдущей функции
        Checking.check_status_code(result_put, 200)
        # msg взято из документации, что приходит в ответе запроса PUT
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        # проверим что адрес изменился
        print("\nМетод GET => PUT")
        result_get = Google_maps_api.get_new_place(place_id)    # сюда передаем place id  с предыдущей функции
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)    # сюда передаем place id  с предыдущей функции
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')


        print("\nМетод GET => DELETE")
        result_get = Google_maps_api.get_new_place(place_id)    # сюда передаем place id  с предыдущей функции
        Checking.check_status_code(result_get, 404)
        Checking.check_json_search_word_in_value(result_get, 'msg', 'Get operation failed')
        print("Тестирование создания, изменения и удаления новой локации прошло успешно!")