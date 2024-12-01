import json


def remove_contact():
    phone_number = input("Enter Phone Number: ")

    # Check if phone number is empty
    if not phone_number:
        print("- Phone Number Field is required -")
        return

    try:
        # load data from JSON
        with open("data.json", "r") as file:
            contacts = json.load(file)
            if len(contacts) == 0:
                print("- Not Found Contacts -")
                return
            # Search and remove the contact
            for i, contact in enumerate(contacts):
                if phone_number == contact["phone_number"]:
                    contacts.pop(i)
                    print(
                        f"- Contact with phone number {phone_number} has been removed -"
                    )
                    break
                else:
                    print(f"- Invalid Phone Number {phone_number} -")
    except FileNotFoundError:
        print("- Not Found Contacts -")
        contacts = []
    except json.JSONDecodeError:
        print("- Error in reading JSON data -")
        contacts = []  # Handle corrupted JSON and initialize an empty list

    # Write updated data back to JSON
    with open("data.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)
