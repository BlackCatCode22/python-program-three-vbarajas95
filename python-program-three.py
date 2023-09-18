# python-program-three.py
#
# Programmer Name: Vanessa Barajas
# Date: 9-17-2023
# Class: CIT 95

# Create an empty list to store contact information:
contacts = []

# Create a function to add a new contact
def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")

    # Create a dictionary for a new contact
    new_contact = {'name': name, 'phone': phone, 'email': email}

 # Append the contact dictionary to the contacts list
    contacts.append(new_contact)
    print("Contact has been successfully added!")

# Create a function to view all contacts:
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print()



# Create a function to search for a function by name
def search_contact():
    name = input("Please enter the name to search for: ")
    found = False

    for contact in contacts:
        if contact['name'] == name:
            print("Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break

    if not found:
        print("Contact not found.")


# Create Main Menu For Contacts
while True:
    print("\nContact Main Menu")
    print("1. Add a New Contact")
    print("2. View Existing Contacts")
    print("3. Search for an Existing Contact")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("ERROR: Invalid choice. Please try again.")


