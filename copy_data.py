from choice_file import choice_number_file_copy
import shutil

def copy():

    number_from, number_in = choice_number_file_copy()  # ИЗ которого копируем, и В который копи..

    # num_copy_row = int(input("Выберите номер строки, которую хотите скопировать: ")) # сделать минус 1
    # while num_copy_row < 0 or num_copy_row > count_rows:
    #     num_copy_row = int(input(f"Ошибка!"
    #                                f"Введите номер строки "
    #                                f"от 1 до {count_rows}: "))
    
    # with open(f'Seminar8_file_system/db/data_{number_from}.txt', 'w+') as file_from, open(f'Seminar8_file_system/db/data_{number_in}.txt', 'w+') as file_in:
    #     shutil.copyfileobj(file_from, file_in)





    with open(f'Seminar8_file_system/db/data_{number_from}.txt', 'r', encoding='utf-8') as file_from:
        data_from = file_from.readlines()

    with open(f'Seminar8_file_system/db/data_{number_in}.txt', 'w+', encoding='utf-8') as file_in:
        file_in.writelines(data_from)
        


copy()