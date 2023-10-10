from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберите файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number

def choice_number_copy_from_file():
    print_file()
    number = int(input("Выберите файл, из которого вы хотите копировать информацию\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number

def choice_number_copy_to_file():
    print_file()
    number = int(input("Выберите файл, в который вы хотите копировать информацию\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number