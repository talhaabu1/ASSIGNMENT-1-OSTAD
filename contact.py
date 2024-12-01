from add_contact import add_contact
from show_contacts import show_contacts
from remove_contact import remove_contact
from search_contacts import search_contacts

while True:
    print("Contact Book Management - choose options ⤵")
    print("0. Exit For Contact -")
    print("1. Create new Contact -")
    print("2. Show All Contacts -")
    print("3. Remove Contact -")
    print("4. Search Contacts -")

    option = input("Chose Options: ")

    if option == "0":
        break
    elif option == "1":
        add_contact()
    elif option == "2":
        show_contacts()
    elif option == "3":
        remove_contact()
    elif option == "4":
        search_contacts()
    else:
        print("Invalid Options -")
