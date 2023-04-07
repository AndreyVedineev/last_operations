import os

from utils.utils import load_file, filter_by_status, sorting_by_date, str_date_str, check_from_to

path_operations = os.path.join('data', 'operations.json')  # путь к файлу


def main():
    file = load_file(path_operations)
    filter_file = filter_by_status(file)
    sort_filter_file = sorting_by_date(filter_file)
    out_print(sort_filter_file)


def out_print(file_sort):
    """
     Выводит в терминал заданную информацию
    """
    for item in file_sort:
        print(str_date_str(item['date']) + ' ' + ' ' + item["description"])
        print(f"{check_from_to(item.get('from'))} --> {check_from_to(item.get('to'))}")
        print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()
