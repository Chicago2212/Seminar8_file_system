from choice_file import choise_file_for_copy
from print_data import print_file

def copy_rows():
    nf = choise_file_for_copy()
    with open (f'db/data_{nf[0]}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = [f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    with open (f'db/data_{nf[1]}.txt', 'r', encoding='utf-8') as file:
        data2 = file.readlines()
    with open(f'db/data_{nf[1]}.txt', 'a+', encoding='utf-8') as file:
        for i in range(len(data)):
            file.write(f'{i+len(data2)+1};{data[i]}')
    print (f"Данные из файла data_{nf[0]}.txt скопированы в файл data_{nf[1]}.txt")