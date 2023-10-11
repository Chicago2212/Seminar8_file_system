from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру от 1 до 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру от 1 до 2: "))
    return number
