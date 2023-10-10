from choice_file import choice_number_file
from choice_file import choice_number_copy_from_file
from choice_file import choice_number_copy_to_file


def data_file():
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf

def data_file_copy_from():
    nf = choice_number_copy_from_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf

def data_file_copy_to():
    nf = choice_number_copy_to_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
