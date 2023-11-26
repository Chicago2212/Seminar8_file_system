from return_data_file import data_file

def copy_row():
    # Чтение данных из исходного файла
    data, nf = data_file()
    count_rows = len(data)
    
    # Получение номера строки от пользователя
    number_row = int(input(f"Введите номер строки от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка! Введите номер строки от 1 до {count_rows}: "))
    
    # Получение имени второго файла
    second_file_name = input("Введите имя второго файла: ")

    # Чтение данных из второго файла
    try:
        with open(f'db/data_{second_file_name}.txt', 'r', encoding='utf-8') as second_file:
            second_file_data = second_file.readlines()
    except FileNotFoundError:
        print(f"Файл data_{second_file_name}.txt не найден.")
        return

    # Копирование строки во второй файл
    second_file_data.append(data[number_row - 1])

    # Запись измененных данных во второй файл
    with open(f'db/data_{second_file_name}.txt', 'w', encoding='utf-8') as second_file:
        second_file.writelines(second_file_data)

    print("Данные успешно скопированы во второй файл!")
