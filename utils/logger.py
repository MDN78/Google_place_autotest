# для фиксации даты и времени тестов
import datetime
import os

class Logger:
    # создание файла который будет храниться в папке logs
    # Прописываем название файла и дату - год месяц день и тд и расширение log
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
    @classmethod
    # (cls) - чтобы метод обращался к переменной класса Logger
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
             logger_file.write(data)

    @classmethod
    # Добавление запроса в файл
    def add_request(cls, url: str, method: str):
        # импортировать библиотеку os
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        # данные для добавления
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"
        # обращаемся к методу write_log_to_file чтобы записать данные в файл
        cls.write_log_to_file(data_to_add)

    # метод ля добавления ответа
    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)
