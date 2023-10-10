from return_data_file import data_file_copy_from
from return_data_file import data_file_copy_to


def copy_file():
    data_from, n_copy = data_file_copy_from()
    data_to, n_to = data_file_copy_to()
    count_rows_from = len(data_from)
    count_rows_to = len(data_to)

    if count_rows_from == 0:
        print("Файл пустой!")
    else:
        number_row_from = int(input(f"Введите номер копируемой строки "
                                    f"от 1 до {count_rows_from}: "))
        while (number_row_from > count_rows_from):
            number_row_from = int(input(f"Введите номер копируемой строки "
                                        f"от 1 до {count_rows_from}: "))

        data_to_write = f"{count_rows_to + 1}" + \
            data_from[number_row_from - 1][1:]
        with open(f'db/data_{n_to}.txt', 'a', encoding='utf-8') as file:
            file.write(data_to_write)
        print("Данные успешно скопированы!\n")
