from return_data_file import data_file


def copy_file():
    data_from, nf_f = data_file()
    count_rows_df = len(data_from)
    if count_rows_df == 0:
        print("Файл пустой!")
    else:
        number_row_df = int(input(f"Введите номер строки "
                                  f"от 1 до {count_rows_df}: "))
        while number_row_df < 1 or number_row_df > count_rows_df:
            number_row_df = int(input(f"Ошибка!"
                                      f"Введите номер строки "
                                      f"от 1 до {count_rows_df}: "))
    nf_t = int(input("Выберите файл, куда скопировать строку\n"
                       "Введите цифру 1 или 2: "))
    while nf_t < 1 or nf_t > 2:
        nf_t = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    with open(f'db/data_{nf_t}.txt', 'r', encoding='utf-8') as file:
        data_to = file.readlines()
    now_number_row = len(data_to) + 1
    with open(f'db/data_{nf_t}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};'
                   f'{data_from[number_row_df-1].split(";")[1]};'
                   f'{data_from[number_row_df-1].split(";")[2]};'
                   f'{data_from[number_row_df-1].split(";")[3]};'
                   f'{data_from[number_row_df-1].split(";")[4]}\n')
        print("Строка успешно скопирована!")
    # print(data_from[number_row_df-1].split(';')[1])

