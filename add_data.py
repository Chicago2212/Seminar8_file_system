from return_data_file import data_file


def add_row():
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    data, nf = data_file()
    now_number_row = len(data) + 1
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{birthdate};{town}\n')
    print("Данные успешно записаны!\n")
