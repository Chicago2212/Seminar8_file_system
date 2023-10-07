from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number


def choise_file_for_copy():
    print_file()
    source_file = int(input("Выберите файл, из которого данные будут скопированы\n"
                            "Введите цифру 1 или 2: "))
    while source_file < 1 or source_file > 2:
        source_file = int(input("Ошибка!!!\n"
                                "Введите цифру 1 или 2: "))
    if source_file == 1:
        result_file = 2
    else:
        result_file = 1
    return [source_file, result_file]
