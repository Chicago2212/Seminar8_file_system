from print_data import print_file

def copy():
    print_file()
    nf = int(input("Выберит файл, из которого будут скопированы данные\n"
                       "Введите цифру 1 или 2: "))
    while nf < 1 or nf > 2:
        nf = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))

    with open(f'Seminar8_file_system/db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()    
    if data == []:
        print('Нечего копировать(')
    else:
        nf2 = 3 - nf
        with open(f'Seminar8_file_system/db/data_{nf2}.txt', 'r', encoding='utf-8') as file:
            data2 = file.readlines()
    
        print(f"Данные из файла data_{nf}.txt буду скопированы в файл data_{nf2}.txt")
        number_row = len(data2) + 1
        data = [f'{number_row + i};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
        with open(f'Seminar8_file_system/db/data_{nf2}.txt', 'a', encoding='utf-8') as file:
            file.writelines(data)
    
        print_file()
        print("Данные успешно скопированы!")

copy()
