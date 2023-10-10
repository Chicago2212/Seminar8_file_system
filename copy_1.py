from return_data_file import data_file_copy_from
from return_data_file import data_file_copy_to


def copy_file():
    data_from, n_copy = data_file_copy_from()
    data_to, n_to = data_file_copy_to()
    count_rows_from = len(data_from)

    if count_rows_from == 0:
        print("Файл пустой!")
    else:
        number_row_from = int(input(f"Введите номер копируемой строки "
                                    f"от 1 до {count_rows_from}: "))

        data_to_copy = data_from[number_row_from - 1]
        print(data_to_copy)
