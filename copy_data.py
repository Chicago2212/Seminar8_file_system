def copy_data():
    number = int(input("Выберит в какой файл из какого скопировать строку\n"
                       "1. data_1.txt --> data_2.txt\n"
                       "2. data_2.txt --> data_1.txt\n"))
    
    number_row = int(input("Введите номер строки: "))

    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    if (number == 1):
        data_1 = open("Seminar8_file_system\db\data_1.txt", "r", encoding='utf-8')
        contents = data_1.readlines()
        stroka = contents[number_row]
        data_2 = open("Seminar8_file_system\db\data_2.txt", "a", encoding='utf-8')
        data_2.writelines(stroka)

    if (number == 2):
        data_2 = open("Seminar8_file_system\db\data_2.txt", "r", encoding='utf-8')
        contents = data_2.readlines()
        stroka = contents[number_row]
        data_1 = open("Seminar8_file_system\db\data_1.txt", "a", encoding='utf-8')
        data_1.writelines(stroka)
    print("Данные успешно записаны!")