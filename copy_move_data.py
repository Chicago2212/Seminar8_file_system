from return_data_file import data_source_and_target_file


def copy_move_row(move = False):
    data_source, data_target, nf_source, nf_target = data_source_and_target_file()
    count_rows = len(data_source)
    buffer_data = []
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        with open(f'db/data_{nf_source}.txt', 'r', encoding='utf-8') as file:
            buffer_data = file.readlines()
            buffer_row = buffer_data[number_row-1].split(";")
        now_number_row = len(data_target) + 1
        with open(f'db/data_{nf_target}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{now_number_row};{buffer_row[1]};'
                   f'{buffer_row[2]};{buffer_row[3]};{buffer_row[4]}')
        if(move):
            del data_source[number_row - 1]
            data_source = [f'{i + 1};{data_source[i].split(";")[1]};'
                    f'{data_source[i].split(";")[2]};'
                    f'{data_source[i].split(";")[3]};'
                    f'{data_source[i].split(";")[4]}'
                    for i in range(len(data_source))]
            with open(f'db/data_{nf_source}.txt', 'w', encoding='utf-8') as file:
                file.writelines(data_source)     
        if(move):
            print("Строка успешно перенесена!")
        else:
            print("Строка успешно скопирована!")