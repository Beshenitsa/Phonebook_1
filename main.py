from delete_file import delete_entry
from entry_file import add_entry
from view_file import view_phonebook
from edit_file import edit_entry
from search_file import search_entry
from create_file import create_phonebook

def run_phonebook():
    print("Menu:")
    print("1. Contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Edit contact")
    print("5. Find contact")
    print("6. Create new contact")
    print("0. Exit")
    while True:    
        choice = input("Input the number: ")

        if choice == "1":
            view_phonebook()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            search_entry()
        elif choice == "6":
            create_phonebook()
        elif choice == "0":
            print("Good buy!")
            break
        else:
            print("Wrong input. Try again, please.")
            print()
            continue

run_phonebook()

    



















# book_dict = {}

# def show_phonebook():
#     with open('phonebook/phonebook.txt', 'r', encoding = 'UTF-8') as file:
#         data = file.read()
#     return data

# def add_contact(name, number):
#     with open('phonebook/phonebook.txt', 'a', encoding='UTF-8') as file:
#         book_dict[name] = number
#         file.write('\n{}: {}'.format(name, number))
#     return book_dict

# def find_contact(name):
#         with open("phonebook/phonebook.txt", 'r', encoding='utf-8') as file:
#             for i in file.readlines():
#                 if i:
#                     key, val = i.strip().split(':')
#                     book_dict[key] = val
#                 for i in book_dict.keys():
#                     if i == name:
#                         return f"{i} - {book_dict[i]} "
#             return "Контакт не найден"
                    
# def change_contact(name, new_name):
#         with open("phonebook/phonebook.txt", 'r', encoding='utf-8') as fh:
#             for i in fh.readlines():
#                 if i:
#                     key, val = i.strip().split(':')
#                     book_dict[key] = val
#                 for i in book_dict.keys():
#                     if i == name:
#                         i = new_name
#                         book_dict.update({new_name})
#                         with open('phonebook/phonebook.txt', 'a', encoding = 'UTF-8') as fhh:
#                             fhh.write('\n{}'.format(new_name))
#                         return "Контакт изменён"
#         return "Контакт не найден"
    
# def delete_contact(name):
#     contact = ''
#     with open("phonebook/phonebook.txt", 'r', encoding='utf-8') as fh:
#             book_dict = {}
#             for i in fh.readlines():
#                 if i.strip() and ':' in i:
#                     key, val = i.strip().split(':')
#                     book_dict[key] = val
#     if name in book_dict:
#         del book_dict[name]
#         with open("phonebook/phonebook.txt", 'w', encoding='utf-8') as fh:
#             book_dict.pop(contact)
#             for key, val in book_dict.items():
#                 fh.write(f'{key}:{val}\n')
#             return "Контакт успешно удалён"
#     return "Контакт не найден"


# flag=True
# while flag:
#     print('''
#     1 - добавить контакт
#     2 - удалить контакт
#     3 - найти контакт
#     4 - показать контакты
#     5 - выйти''')
#     answer = input("\nЧто вы хотите сделать введите 1,2,3, или 4 если хотите выйти: " )
#     if answer == '1':
#         insert_name = input("Enter name contact: ")
#         insert_number = input('Ennter number contact: ')
#         print(add_contact(name = insert_name, number = insert_number))
#         print('Контакт успешно создан!')
#     if answer == '2':
#         insert_name = input("Enter name contact: ")
#         print(delete_contact(name = insert_name))
#     if answer =='3':
#         insert_name = input("Enter name contact: ")
#         print(find_contact(name = insert_name))
#     if answer == '4':
#         print(show_phonebook())
#     if answer == '5':
#         flag=False
# print('Good buy'.upper())