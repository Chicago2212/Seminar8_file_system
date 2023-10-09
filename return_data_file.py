from choice_file import choice_number_file


def data_file():  # открывает для чтения файл по выбранному номеру nf
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
