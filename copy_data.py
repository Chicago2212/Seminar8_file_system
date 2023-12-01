from return_data_file import data_file


def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер копируемой строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер копируемой строки "
                               f"от 1 до {count_rows}: "))
    if nf == 1:
        nf_choosen = 2
    else:
        nf_choosen = 1

    with open(f'db/data_{nf_choosen}.txt', 'r', encoding='utf-8') as file:
        data_1 = file.readlines()
        now_number_row = len(data_1) + 1
        data_2 = data[number_row - 1].split(";")
        print(data_2[0])
        with open(f'db/data_{nf_choosen}.txt', 'a', encoding='utf-8') as file:
            file.write(
                f"{now_number_row};{data_2[1]};{data_2[2]};{data_2[3]};{data_2[4]}")

    print("Данные успешно скопированы!")
