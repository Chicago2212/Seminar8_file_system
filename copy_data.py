def copy_file():
    path ='db/'+ input("Введите имя файла для копирования (без расширения) ")+'.txt'
    print(path)
    with open(path, 'r') as file1:
        with open('db/data_1.txt', 'a') as file2:
            data = file1.read()
            file2.write(data)
    print(f'Данные из файла {path} успешно скопированы в "db/data_1.txt"')

