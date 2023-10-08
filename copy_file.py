from return_data_file import data_file

def copy_file():
    data, nf = data_file()
    if nf == 2:
        with open('db/data_1.txt','r',encoding='utf-8') as file:
            data1 = file.readlines()
        with open('db/data_2.txt','r',encoding='utf-8') as file:
            data2 = file.readlines()
        number = len(data2)
        new_data = []
        for i in data1:
            i = i.replace(f'{i[0]}',f'{number + 1}')
            new_data.append(i)
            number+=1


        with open('db/data_2.txt','a',encoding='utf-8') as file:
            file.writelines(new_data)
        print("Все данные из файла 1 скопированы в файл 2 успешно!")
    else:
        with open('db/data_2.txt','r',encoding='utf-8') as file:
            data1 = file.readlines()
        with open('db/data_1.txt', 'r', encoding='utf-8') as file:
            data2 = file.readlines()
        number = len(data2)
        new_data = []
        for i in data1:
            i = i.replace(f'{i[0]}', f'{number + 1}')
            new_data.append(i)
            number += 1

        with open('db/data_1.txt','a',encoding='utf-8') as file:
            file.writelines(new_data)
        print("Все данные из файла 2 скопированы в файл 1 успешно!")
copy_file()

