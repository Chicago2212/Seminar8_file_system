from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number

def choice_number_file_clone():
    print_file()
    number_clone = int(input("Выберит файл, в который хотите перенести данные\n"
                       "Введите цифру 1 или 2: "))
    while number_clone < 1 or number_clone > 2:
        number_clone = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number_clone

