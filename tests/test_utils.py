import os

from utils.utils import load_file, check_from_to, str_date_str, filter_by_status

path_operations = os.path.join('..', 'data', 'operations.json')


def test_load_file():
    assert type(load_file(path_operations)) == list


def test_filter_by_status():
    file = load_file(path_operations)
    file_1 = filter_by_status(file)
    for i in file_1:
        assert i['state'] == "EXECUTED"


def test_str_date_str():
    assert str_date_str('2019-12-08T22:46:21.935582') == "08.12.2019"


def test_check_from_to():
    assert check_from_to("Счет 90424923579946435907") == "Счет **5907"
    assert check_from_to("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert check_from_to(None) == "========"

