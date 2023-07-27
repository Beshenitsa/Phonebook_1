def edit_entry():
    name = input("Введите ФИО для редактирования записи: ")
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        file.write(lines[0])
        for line in lines[1:]:
            if name.lower() in line.lower():
                print("Найдена запись:")
                print(line.strip())
                new_name = input("Введите новое ФИО: ")
                new_phone_number = input("Введите новый номер телефона: ")
                file.write(f"{new_name},{new_phone_number}\n")
                print("Запись успешно отредактирована.")
            else:
                file.write(line)
