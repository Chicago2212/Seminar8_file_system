from choice_file import choice_number_file
from return_data_file import data_file


def copy_data():
    data = data_file()
    next_row = len(data)
    source_nf = int(input("Выберите из какого файла будем копировать: "))

    destination_nf = int(input("Выберите в какой файл будем копировать: "))

    if destination_nf == source_nf:
        print("Выберите файл, который не совпадает с копируемым: ")
        destination_nf = int(input("Выберите в какой файл будем копировать: "))
    else:
        res = f"{next_row + 1};{name};{surname};{birthdate};{town}\n"
        with open(f"db/data_{destination_nf}.txt", 'a', encoding="utf-8") as file:
            file.writelines(res)

print("Данные успешно скопированы!")













# from choice_file import choice_number_file
# def copy_data():
#     print("Выберите файл-источник:")
#     source_nf = choice_number_file()
#     with open(f'db/data_{source_nf}.txt', 'r', encoding='utf-8') as file:
#         source_data = file.readlines()
#
#     print("Выберите файл-приемник:")
#     target_nf = choice_number_file()
#     while target_nf == source_nf:  # Убеждаемся, что файлы не одинаковые
#         print("Файл-приемник не должен совпадать с файлом-источником. Пожалуйста, выберите другой файл.")
#         target_nf = choice_number_file()
#
#     with open(f'db/data_{target_nf}.txt', 'a', encoding='utf-8') as file:
#         file.writelines(source_data)
#
#     print(f"Данные из файла {source_nf} были успешно скопированы в файл {target_nf}!")