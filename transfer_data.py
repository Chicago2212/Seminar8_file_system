from delete_data import delete_row


def check_input(message, range_limit):
    if isinstance(message, str):
        help_msg = "Введите цифру 1 или 2: "
        user_input = int(input(message + "\n" + help_msg))
        while user_input < 1 or user_input > range_limit:
            user_input = int(input("Ошибка!!!\n" + help_msg))
        return user_input
    elif isinstance(message, list):
        user_input = message
        flag = True
        while flag:
            for i in user_input:
                if i > range_limit:
                    user_input = [
                        int(i)
                        for i in input(
                            "Неверный ввод! "
                            "Пожалуйста введите номера строк через пробел: "
                        )
                        .strip()
                        .split()
                    ]
                else:
                    flag = False
        return user_input


def get_file_data(path):
    with open(f"db/data_{path}.txt", "r", encoding="utf=8") as file:
        data = file.readlines()
    return data


def prepare_data_to_transfer(src, lines):
    src_data = get_file_data(src)

    string_clip = []
    for i in lines:
        string_clip.append(src_data[i - 1])
    return string_clip


def copy_data(src, dst, lines):
    string_clip = prepare_data_to_transfer(src, lines)
    current_index = len(get_file_data(dst)) + 1

    with open(f"db/data_{dst}.txt", "a", encoding="utf=8") as dst_file:
        for i in range(len(string_clip)):
            dst_file.write(
                f"{current_index + i};{string_clip[i].split(';')[1]};"
                f"{string_clip[i].split(';')[2]};{string_clip[i].split(';')[3]};"
                f"{string_clip[i].split(';')[4]}"
            )


def move_data(src, dst, lines):
    copy_data(src, dst, lines)
    string_clip = prepare_data_to_transfer(src, lines)
    src_data = get_file_data(src)

    for line in src_data:
        if line in string_clip:
            del src_data[src_data.index(line)]

    src_data = [
        f'{i + 1};{src_data[i].split(";")[1]};'
        f'{src_data[i].split(";")[2]};'
        f'{src_data[i].split(";")[3]};'
        f'{src_data[i].split(";")[4]}'
        for i in range(len(src_data))
    ]
    with open(f"db/data_{src}.txt", "w", encoding="utf-8") as file:
        file.writelines(src_data)


def transfer_data():
    src_file = check_input("Выберите исходный файл", 2)
    dst_file = check_input("Выберите файл назначения", 2)
    lines_limit = len(get_file_data(src_file))
    if src_file == dst_file:
        print(
            "Операция невозможна: исходный файл и файл назначения должны быть разными"
        )
        return
    operation_type = check_input(
        "Выберите тип операции: копировать(1)/переместить(2)", 2
    )
    lines = check_input(
        [
            int(i)
            for i in input(f"Введите строки от 1 до {lines_limit} через " f"пробел: ")
            .strip()
            .split()
        ],
        lines_limit,
    )
    if operation_type == 1:
        copy_data(src_file, dst_file, lines)
        print("Данные успешно скопированы")
    elif operation_type == 2:
        move_data(src_file, dst_file, lines)
        print("Данные успешно перенесены")
