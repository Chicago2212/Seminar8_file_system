from return_data_file import data_file


def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    copied = data[number_row - 1]
    data, nf = data_file()
    count_rows = len(data) + 1
    name = copied.split(";")[1]
    surname = copied.split(";")[2]
    birthdate = copied.split(";")[3]
    town = copied.split(";")[4]
    copied= f'{count_rows};{name};{surname};{birthdate};{town}\n'
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.writelines(copied)
    print("Строка успешно скопирована!")
    

    
    
         







