import json


def add_contact():

    #  enter contact info
    name = input("Enter Name: ").strip()

    if not name or not name.isalpha():
        print("Name is required. Name must be a string.")
        name = input("Enter Name: ")

    phone_number = input("Enter Phone Number: ").strip()

    if not phone_number or not phone_number.isdigit():
        print("Phone Number is required. Phone Number must be a digit.")
        phone_number = input("Enter Phone Number: ")

    email = input("Enter Email: ").strip()

    if not email:
        print("Email is required.")
        email = input("Enter Email: ")

    address = input("Enter Address: ").strip()

    if not address:
        print("Address is required.")
        address = input("Enter Address: ")

    # contact info
    contact_info = {
        "name": name.title(),
        "phone_number": phone_number,
        "email": email,
        "address": address.title(),
    }

    #  load data from JSON
    try:
        with open("data.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

    # handel Prevent Duplicate Numbers
    for contact in contacts:
        if phone_number == contact["phone_number"]:
            print(f"- Already Exist {contact["phone_number"]} -")
            return

    # add append in contacts
    contacts.append(contact_info)

    # Write updated data back to JSON
    with open("data.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)
