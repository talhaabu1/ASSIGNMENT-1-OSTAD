import json


def show_contacts():
    try:
        #  load data from json
        with open("data.json", "r") as file:
            contacts = json.load(file)
            # check length data is not 0
            if len(contacts) == 0:
                print("- Not Found Contacts -")
                return
            # print user contacts info
            for i, contact in enumerate(contacts, start=1):
                print(
                    f"{i}. {contact['name']} - {contact['phone_number']} - {contact['email']} - {contact['address']} "
                )
    except FileNotFoundError:
        print("- Not Found Contacts -")
    except json.JSONDecodeError:
        print("- Error in reading JSON data -")
