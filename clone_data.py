from return_data_file import data_file
from return_data_file import data_file_clone


def clone_data():
    data, nf = data_file()  # изменяемый
    count_rows = len(data)

    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер копируемой строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))

        data_clone, nfc = data_file_clone()  # клонируемый
        now_number_clone_row = len(data_clone) + 1
        with open(f'db/data_{nfc}.txt', 'a', encoding='utf-8') as file:
            file.writelines(f'{now_number_clone_row};'
                            f'{data[number_row - 1].split(";")[1]};'
                            f'{data[number_row - 1].split(";")[2]};'
                            f'{data[number_row - 1].split(";")[3]};'
                            f'{data[number_row - 1].split(";")[4]}')

    print("Данные успешно скопированы!")
