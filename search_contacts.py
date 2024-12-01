import json


def search_contacts():
    name = input("Enter Name: ").strip()

    if not name or not name.isalpha():
        print("Name is required. Name must be a string.")
        name = input("Enter Name: ")

    try:
        #  load data from json
        with open("data.json", "r") as file:
            contacts = json.load(file)
            # check length data is not 0
            if len(contacts) == 0:
                print("- Not Found Contacts -")
                return
                # handel Prevent Duplicate Numbers
            for contact in contacts:
                if name.lower() == contact["name"].lower():
                    print(
                        f"-. {contact['name']} - {contact['phone_number']} - {contact['email']} - {contact['address']} "
                    )
                    break
                else:
                    print("- Not Found Contacts -")

    except FileNotFoundError:
        print("- Not Found Contacts -")
    except json.JSONDecodeError:
        print("- Error in reading JSON data -")
