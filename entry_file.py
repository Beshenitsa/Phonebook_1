import re

def add_entry():
    name = input("Input full name: ")
    while True:
        phone_number = input("Input phone number: ")
        if re.match(r'^(\+7|8)[\d]{10}$', phone_number):
            if phone_number.startswith('8'):
                phone_number = '+7' + phone_number[1:]
            break
        else:
            print("Wrong format. Please, input phone this way +7XXXXXXXXXX, or this way 8XXXXXXXXXX.")
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(f"{name},{phone_number}\n")
    print("Contact added.")


