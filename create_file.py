def create_phonebook():
    with open("phonebook.txt", "w", encoding="utf-8") as file:
        file.write("Full name, Phone number\n")
    print("Contact book created.")

create_phonebook()