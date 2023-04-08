import json
import os
from datetime import datetime

number_of_operations = 5  # количество последних операций


def load_file(path):
    """
    Загружает список операций из файла
    :param path:   из файла data/operations.json')--
    :return: список словарей из json данные операций
    """
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def filter_by_status(file):
    """
    :return: Возвращает список успешных операций клиента
    """
    executed_opertions = [x for x in file if 'state' in x and x['state'] == "EXECUTED"]
    return executed_opertions


def sorting_by_date(file) -> list:
    """
   :return: возвращает отсортированный по "date" список последних {number_of_operations} операций клиента
    """
    return sorted(file, key=lambda x: x["date"], reverse=True)[:number_of_operations]


def str_date_str(date_time_string):
    """
    Привидение к желаемому формату даты
    :param date_time_string: строкое значение даты и времени
    :return: строковое значение даты в формате число, месяц, год
    """
    date_obj = datetime.strptime(date_time_string, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_obj.date(), '%d.%m.%Y')


def check_from_to(_form):
    """
    :param _form:   Подготовка номера карты или счета, поиск первого числа в строке,
                    маскирование ХХХХ ХХ** **** ХХХХ - карты, счет **ХХХХ
    :return: маскированую строку
    """
    if _form:
        ch = ""
        for i in _form:
            if i.isdigit():
                ch += i
        str_out = _form[:_form.find(ch) - 1]  # символьная часть _form - значения поля "from"
        numbers_out = _form[_form.find(ch):]  # цифровая часть _form - значения поля "from"
        if len(numbers_out) == 16:  # номер карты 16 цифр
            numbers_out = numbers_out[:4] + ' ' + numbers_out[4:6] + "**" + " " + "****" + " " + numbers_out[-4:]
        elif len(numbers_out) == 20:  # счет имеет 20 цифр
            numbers_out = "**" + numbers_out[-4:]
        return f"{str_out} {numbers_out}"
    else:
        return ("VVVVVVVV")
