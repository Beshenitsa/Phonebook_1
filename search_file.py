def search_entry():
    keyword = input("INput a word to search with: ")
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
        found_entries = []
        for line in lines[1:]:
            if keyword.lower() in line.lower():
                found_entries.append(line.strip())
        if found_entries:
            print("The contacts found:")
            for entry in found_entries:
                print(entry)
        else:
            print("Contact is not found.")