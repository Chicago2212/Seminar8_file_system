from choice_file import choice_number_file
from return_data_file import data_file
from print_data import print_file


def copy_data():
    print_file()
    source_nf = int(input("Какой файл будем копировать, 1 или 2: "))
    with open(f'db/data_{source_nf}.txt', 'r', encoding='utf-8') as file:
        source_data = file.readlines()
        print(source_data)

    destination_nf = int(input("Выберите в какой файл будем вставлять данные: "))
    # with open(f'db/data_{destination_nf}.txt', 'r', encoding='utf-8') as file:
    #     destination_data = file.readlines()
        print(destination_data)

    while destination_nf == source_nf:
        destination_nf = int(input("Ошибка!\n"
                      "Выберите файл, который не совпадает с копируемым."
                      "Выберите в какой файл будем вставлять данные: "))

    # data = data_file()
    # now_number_row = len(data) + 1

    with open(f"db/data_{destination_nf}.txt", 'a', encoding="utf-8") as file:
        file.writelines(source_data)
    print("Данные успешно скопированы!")
    # print(source_data)












# from print_data import print_file
# # from choice_file import choice_number_file
# def copy_data():
#     print("Выберите файл-источник:")
#     source_nf = print_file()
#     with open(f'db/data_{source_nf}.txt', 'r', encoding='utf-8') as file:
#         source_data = file.readlines()
#
#     print("Выберите файл-приемник:")
#     target_nf = print_file()
#     while target_nf == source_nf:  # Убеждаемся, что файлы не одинаковые
#         print("Файл-приемник не должен совпадать с файлом-источником. Пожалуйста, выберите другой файл.")
#         target_nf = print_file()
#
#     with open(f'db/data_{target_nf}.txt', 'a', encoding='utf-8') as file:
#         file.writelines(source_data)
#
#     print(f"Данные из файла {source_nf} были успешно скопированы в файл {target_nf}!")



#
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