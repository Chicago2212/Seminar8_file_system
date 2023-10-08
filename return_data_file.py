from choice_file import choice_number_file
from choice_file import choice_number_file_clone


def data_file():
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf

def data_file_clone():
    nfc = choice_number_file_clone()
    with open(f'db/data_{nfc}.txt', 'r', encoding='utf-8') as file:
        data_clone = file.readlines()
    return data_clone, nfc
