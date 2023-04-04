import json
import os
from operator import itemgetter

path_operations = os.path.join('..', 'data', 'operations.json')  # путь к файлу
number_of_operations = 5


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


def filter_by_status():
    """
    :return: возвращает отсортированный по "date" список последних {number_of_operations} операций клиента
    """
    file = load_file(path_operations)
    executed_opertions = []
    for item in file:
        if not item:
            continue
        if item['state'] == "EXECUTED":
            executed_opertions.append(item)
    return executed_opertions


def sorting_by_date() -> list:
    """
   :return: возвращает отсортированный по "date" список последних {number_of_operations} операций клиента
    """
    date_operations = filter_by_status()
    return sorted(date_operations, key=itemgetter('date'), reverse=True)[0:number_of_operations]


# a = sorting_by_date()
# for i in a:
#     print(i)
