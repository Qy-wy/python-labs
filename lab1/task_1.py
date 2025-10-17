def format_fio():
    fio = input("Введите ФИО через пробел: ")
    fio_parts = fio.split()
    if len(fio_parts) < 3 :
        print("Некорректный ввод")
        return
    surname, name, patronymic = fio_parts
    new_format_fio = f"{surname} {name[0]}.{patronymic[0]}"
    print("Result: ", new_format_fio)

format_fio()
