from return_data_file import data_file


def transfer_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        if nf == 1:
            nf_1 = 2
        else:
            nf_1 = 1
        with open(f'db/data_{nf_1}.txt', 'r', encoding='utf-8') as file:
            data_1 = file.readlines()
        now_number_row = len(data_1) + 1
        data_2 = data[number_row - 1].split(";")
        print(data_2[0])
        with open(f'db/data_{nf_1}.txt', 'a', encoding='utf-8') as file:
            file.write(f"{now_number_row};{data_2[1]};{data_2[2]};{data_2[3]};{data_2[4]}")

        del data[number_row - 1]
        data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        print("Данные успешно перенесены")