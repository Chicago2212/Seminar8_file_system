from return_data_file import data_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    nf_b = 3 - nf
    with open(f'D:\phyton\Seminar8_file_system_1\db\data_{nf_b}.txt', 'r', encoding='utf-8') as file:
        data_b = file.readlines()
    number_row_b = len(data_b) + 1
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        row_new = data[number_row-1].split(';')
        with open(f'D:\phyton\Seminar8_file_system_1\db\data_{nf_b}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{number_row_b};{row_new[1]};{row_new[2]};{row_new[3]};{row_new[4]}')
        


