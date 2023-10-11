def print_file():
    for i in range(1, 3):
        with open(f'Seminar8_file_system/db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"Вывод данных из {i}-ого файла:\n"
              f"{''.join(data)}")
        print()
