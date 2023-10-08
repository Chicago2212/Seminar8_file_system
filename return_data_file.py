from choice_file import choice_number_file_main


def data_file():
    nf = choice_number_file_main()
    with open(f'Seminar8_file_system/db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
