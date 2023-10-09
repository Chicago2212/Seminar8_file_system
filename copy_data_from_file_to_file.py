from choice_file import choice_number_file


def copy_data_from_file():
    print("Путь к источнику копирования")
    input_file=choice_number_file()
    print("Выберите конечный файл для копирования")
    output_file=choice_number_file()
    clear_output = input("Хотите удалить содержимое конечного файла (Y/N)? ").strip().lower()
    with open(f'db/data_{output_file}.txt', 'r',encoding='utf-8') as sizeofoutputfile:
        output_row = len(sizeofoutputfile.readlines())

    if clear_output == 'y':
        with open(f'db/data_{output_file}.txt', 'w',encoding='utf-8') as clearfile:
                clearfile.truncate()
                clearfile.close
        with open(f'db/data_{input_file}.txt', 'r',encoding='utf-8') as infile, open(f'db/data_{output_file}.txt', 'a',encoding='utf-8') as outfile:
            lines = infile.readlines()
            nowrow = len(lines)
            outfile.writelines([f'{i+1};{lines[i].split(";")[1]};'
                f'{lines[i].split(";")[2]};'
                f'{lines[i].split(";")[3]};'
                f'{lines[i].split(";")[4]}'
                for i in range(len(lines))])
    else:
        with open(f'db/data_{input_file}.txt', 'r',encoding='utf-8') as infile, open(f'db/data_{output_file}.txt', 'a',encoding='utf-8') as outfile:
            lines = infile.readlines()
            output_row+=1
            outfile.writelines([f'{output_row+i};{lines[i].split(";")[1]};'
                f'{lines[i].split(";")[2]};'
                f'{lines[i].split(";")[3]};'
                f'{lines[i].split(";")[4]}'
                for i in range(len(lines))])    
    print(f"Данные успешно скопированы из data_{input_file}.txt' в data_{output_file}.txt")
