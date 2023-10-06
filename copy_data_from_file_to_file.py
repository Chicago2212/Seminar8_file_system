from choice_file import choice_number_file


def copy_data_from_file():
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

