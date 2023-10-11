from print_data import print_file


def copy_number_file():
    print_file()
    number = int(input("Выберите файл, с которым хотите работать. \n"
                       "Введите цифру 1 или 2: \n"))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!! \n"
                           "Введите цифру 1 или 2: \n"))

    with open(f'Seminar8_file_system/db/data_{number}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    if number == 2:
        number += 1
    else:
        number += 2

    with open(f'Seminar8_file_system/db/data_{number}.txt', 'a', encoding='utf-8') as file:
        for line in data:
            file.write(line)

    print("Данные успешно скопированы!")
