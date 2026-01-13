# Store contacts with name, phone number, and email
# Menu options:

# Add contact
# View all contacts
# Search contact by name
# Delete contact
# Exit


import os
import json

filename = 'contact.json'

if os.path.exists(filename):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except json.JSONDecodeError:
        contacts = {}
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)

else:
    contacts = {}

def save_contact():
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input('Name: ').strip()
    phone = input('Phone: ').strip()
    email = input('Email: ').strip()

    contacts[name] = {
        'Phone': phone,
        'Email': email
    }
    save_contact()
    print('Contact Added Successfully')

def view_contacts():
    for name, info in contacts.items():
        print(f'Name: {name}')
        print(f'Phone: {info['Phone']}')
        print(f'Email: {info['Email']}')
        print('*'*50)

def search_contacts():
    user_search = input('Enter name to search:\n').lower().strip()
    for name, info in contacts.items():
        if name.lower() == user_search:
            print(f'Name: {name}')
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            return
    print('Name not Found')
    return

def delete_contacts():
    user_delete = input('Enter a name to delete:\n').lower().strip()
    for name in list(contacts.keys()):
        if name.lower() == user_delete:
            del contacts[name]
            save_contact()
            print('Deleted successfully')
            return
    print('Name not found')


while True:
    print('------Contact Book------')
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contact')
    print('4. Delete Contact')
    print('5. Quit')

    try:
        user_choice = int(input('Enter a number (1-5): '))
        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            view_contacts()
        elif user_choice == 3:
            search_contacts()
        elif user_choice == 4:
            delete_contacts()
        elif user_choice == 5:
            print('GoodBye')
            break
    except ValueError:
        print('Enter a valid number')