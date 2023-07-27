def delete_entry():
    name = input("Input full name to delete contact: ")
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("phonebook.txt", "w", encoding="utf-8") as file:
        file.write(lines[0])
        for line in lines[1:]:
            if name.lower() not in line.lower():
                file.write(line)
    print("Contact deleted.")
    
        
    