from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from copy_move_data import copy_move_row
from print_data import print_file


def menu_txt():
    return ("Выберите функцию:\n"
            "1. Добавить\n"
            "2. Удалить\n"
            "3. Изменить\n"
            "4. Копировать\n"
            "5. Переместить\n"
            "6. Вывод\n"
            "7. Выход\n"
            "Введите номер команды: ")



def check_number(n):
    while n < 1 or n > 7:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 7\n" + menu_txt()))
    return n


def start_menu():
    command = None
    while command != 7:
        command = int(input("Доброго времени суток!  Введите цифру от 1 до 7\n" + menu_txt()))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            copy_move_row(False)
        elif command == 5:
            copy_move_row(True)
        elif command == 6:
            print_file()
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)")