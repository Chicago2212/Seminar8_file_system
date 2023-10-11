from return_data_file import data_file
from choice_file import choice_number_file


def copy_row():
    data, nf = data_file()  # открывает для чтения файл по выбранному номеру nf
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    nf2 = choice_number_file()
    with open(f'db/data_{nf2}.txt', 'w', encoding='utf-8') as file:
        file.write(data[number_row - 1])
    print("Данные успешно скопированы!")
