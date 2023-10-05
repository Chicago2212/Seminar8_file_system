from return_data_file import data_file

def copy_file():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows} для копирования: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows} для копирования: "))        
    if nf == 1:
        with open(f'db/data_1.txt', 'r', encoding='utf-8') as file_1, open(f'db/data_2.txt', 'a', encoding='utf-8') as file_2:
            line = file_1.readlines()     
            new_line = line[number_row - 1].split(';')
            with open(f'db/data_2.txt', 'r', encoding='utf-8') as file_new:
                new_line[0] = str(len(file_new.readlines()) + 1)
            new_line =';'.join(new_line)
            file_2.writelines(new_line)            
    else:
        with open(f'db/data_2.txt', 'r', encoding='utf-8') as file_2, open(f'db/data_1.txt', 'a', encoding='utf-8') as file_1:
            line = file_2.readlines()
            new_line = line[number_row - 1].split(';')
            with open(f'db/data_1.txt', 'r', encoding='utf-8') as file_new:
                new_line[0] = str(len(file_new.readlines()) + 1)
            new_line =';'.join(new_line)
            file_1.writelines(new_line)
    print("Строка успешно скопирована в другой файл!")
    
                 
copy_file()    