from choice_file import choice_number_file
from return_data_file import data_file


def copy_data():
    source_nf = int(input("Какой файл будем копировать, 1 или 2: "))
    with open(f'db/data_{source_nf}.txt', 'r', encoding='utf-8') as file:
        source_data = file.readlines()

    destination_nf = int(input("Выберите в какой файл будем вставлять данные: "))

    while destination_nf == source_nf:
        destination_nf = int(input("Ошибка!\n"
                                   "Выберите файл, который не совпадает с копируемым."
                                   "Выберите в какой файл будем вставлять данные: "))

    with open(f"db/data_{destination_nf}.txt", 'a', encoding="utf-8") as file:
        file.writelines(source_data)
        print("Данные успешно скопированы!")
        print()
