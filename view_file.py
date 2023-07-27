def view_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            for line in lines[1:]:
                print(line.strip())
        else:
            print("Contact book is empty.")
