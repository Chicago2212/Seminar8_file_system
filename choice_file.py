from print_data import print_file


def choice_number_file_main():
    print_file()
    number_for_work = int(input("Выберите файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while number_for_work < 1 or number_for_work > 2:
        number_for_work = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number_for_work


def choice_number_file_copy():
    print_file()
    number_for_copy = int(input("Выберите файл, ИЗ которого Вы хотите копировать.\n"
                       "Введите цифру 1 или 2: "))
    while number_for_copy < 1 or number_for_copy > 2:
        number_for_copy = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    
    number_in = int(input("Выберите файл, В который Вы хотите скопировать.\n"
                       "Введите цифру 1 или 2: "))
    while number_for_copy < 1 or number_for_copy > 2:
        number_for_copy = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
        
    return number_for_copy, number_in