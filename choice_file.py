from print_data import print_file


def choice_number_file():
    print_file()
    number = int(input("Выберите файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number


def choice_source_and_target_number_file():
    print_file()
    num_source = int(input("Выберите файл, из которого Вы хотите скопировать\\переместить данные\n"
                       "Введите цифру 1 или 2: "))
    while num_source < 1 or num_source > 2:
        num_source = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    if(num_source == 1):
        num_target = 2
    else: num_target = 1
    return num_source, num_target