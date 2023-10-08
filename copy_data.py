from print_data import print_file


def copy_data():
    print()
    print_file()
    number1 = int(
        input(
            "Выберите файл, данные которого вы хотите скопировать. \n"
            "Введите цифру 1 или 2: "
        )
    )
    while number1 < 1 or number1 > 2:
        number1 = int(input("Ошибка!!! Введите цифру 1 или 2: "))

    with open(f"db/data_{number1}.txt", "r", encoding="utf-8") as file1:
        data1 = file1.readlines()
    count_rows1 = len(data1)
    if count_rows1 == 0:
        print("Файл пустой!")

    else:
        if number1 == 1:
            file_rec_num = 2
        else:
            file_rec_num = 1

        with open(f"db/data_{file_rec_num}.txt", "r", encoding="utf-8") as file2:
            data2 = file2.readlines()
            now_number_row = len(data2) + 1
        data3 = []
        for i in range(len(data1)):
            data3.append(
                f'{now_number_row};{data1[i].split(";")[1]};'
                f'{data1[i].split(";")[2]};'
                f'{data1[i].split(";")[3]};'
                f'{data1[i].split(";")[4]}'
            )
            now_number_row += 1

        with open(f"db/data_{file_rec_num}.txt", "a", encoding="utf-8") as file2:
            file2.writelines(data3)
        print()
        print(
            f"Все данные из файла data_{number1}.txt успешно добавлены в файл data_{file_rec_num}.txt"
        )
        print()
