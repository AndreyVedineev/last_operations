from utils.utils import load_file, filter_by_status, check_from_to
import os

path_operations = os.path.join('..', 'data', 'operations.json')


def test_load_file():
    assert type(load_file(path_operations)) == list


def test_filter_by_status():
    for i in filter_by_status():
        assert i['state'] == "EXECUTED"


def test_check_from_to():
    assert check_from_to("Счет 90424923579946435907") == "Счет **5907"
    assert check_from_to("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"

