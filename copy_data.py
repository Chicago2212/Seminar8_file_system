from return_data_file import data_file


def copy_row():
    data, nf = data_file()
    if nf == 1:
        nf_2 = 2
    else:
        nf_2 = 1
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    data = data[number_row - 1].split(';')
    name = data[1]
    surname = data[2]
    birthdate = data[3]
    town = data[4]
    with open(f'db/data_{nf_2}.txt', 'r', encoding='utf-8') as file:
        data_2 = file.readlines()
    now_number_row = len(data_2) + 1
    with open(f'db/data_{nf_2}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{birthdate};{town}')
    print("Данные успешно скопированы!")
