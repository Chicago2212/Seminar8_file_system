from choice_file import choice_number_file
from choice_file import choice_source_and_target_number_file


def data_file():
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf


def data_source_and_target_file():
    nf_source, nf_target = choice_source_and_target_number_file()
    with open(f'db/data_{nf_source}.txt', 'r', encoding='utf-8') as file:
        data_source = file.readlines()
    with open(f'db/data_{nf_target}.txt', 'r', encoding='utf-8') as file:
        data_target = file.readlines()
    return data_source, data_target, nf_source, nf_target