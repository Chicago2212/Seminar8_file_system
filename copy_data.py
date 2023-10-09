from choice_file import choice_number_file_copy
import shutil


def copy(input_mode):

    number_from, number_in = choice_number_file_copy()  # ИЗ которого копируем, и В который копируем

    with open(f'Seminar8_file_system/db/data_{number_from}.txt', 'r', encoding='utf-8') as file_from: data_from = file_from.readlines()

    count_rows = len(data_from)
    input_mode = user_enter()
    array_rows = []  # массив, в котором будут либо номера строк, либо диапазон.

    if input_mode == 2: 
        while len(array_rows) != 2: 
            row2 = int(input("Введите значение: "))
            while row2 > count_rows: row2 = int(input("Ошибка: такой строки нет! Введите значение повторно: "))
    else: 
        row1 = input("Введите номер(-а) строк(-и) через ',' : ")
        for i in range(array_rows.append(int(row1.split(', ')))): 
            if array_rows[i] > count_rows: 
                array_rows[i] = int(input(f"{i}-ый элемент больше кол-ва строк из исходного файла! Введите его повторно: "))


    with open(f'Seminar8_file_system/db/data_{number_in}.txt', 'w+', encoding='utf-8') as file_in: 
        if input_mode == 1: 
            for i in array_rows: file_in.writelines(data_from[i])
        else: file_in.writelines(data_from[array_rows[0]:array_rows[1]])
        print("Данные успешно скопированы! ")


def user_enter():

    while True:
        try:
            input_mode = int(input("Выберите режим ввода: \n"
                                "1. По номерам строки(одинарный).\n"
                                "2. Диапозон(от и до).\n"
                                "Выбор: "))
        except ValueError: 
            print("Неверный ввод! Введите целое число.")
            continue
        else: break
    while input_mode < 0 or input_mode > 2:
        input_mode = int(input("Ошибка! Выберите 1 или 2."
                                "1. По номерам строки(одинарный).\n"
                                "2. Диапозон(от и до).\n"
                                "Выбор: "))
    return input_mode

 # Через модуль shutil(полное копирование): 
    # with open(f'Seminar8_file_system/db/data_{number_from}.txt', 'w+') as file_from, open(f'Seminar8_file_system/db/data_{number_in}.txt', 'w+') as file_in:
    #     shutil.copyfileobj(file_from, file_in)

# конструкции try - except повсюду писать не стал, так как этот код и без того мне кажется не сокращенным(
