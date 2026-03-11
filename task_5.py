contacts={}

def add_contacts():
    name=input("Enter the contact name:")
    num=input("Enter the contact number:")
    email=input("Enter the contact email:")
    address=input("aenter the contact address:")
    contacts[name]={
        "number":num,
        "email":email,
        "address":address
    }
    print(f"contact '{name}' added successfully!")

def view_saved_contacts():
    print("saved contacts:....")
    if not contacts:
        print("no contacts found.")
        return
    for name, details in contacts.items():
        print(f"name: {name}")
        print(f"Number: {details['number']}")
        print(f"email: {details['email']}")
        print(f"address: {details['address']}")
        print('--------------')

def search_contacts():
    search=input("Enter the contact name or number to search:")
    found = [name for name, details in contacts.items() if search.lower() in name.lower() or search.lower() in details['number'].lower()]
    if found:
        print("search results:")
        for name in found:
            details = contacts[name]
            print(f"Name: {name}")
            print(f"Number: {details['number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("--------")
    else:
        print("No contacts found matching the search criteria.")



def update_contacts():
    name=input("Enter the new contact name to update:")
    if name in contacts:
        num=input("Enter the new contact number:")
        email=input("Enter the new contact email:")
        address=input("Enter the new contact addrss:")
        contacts[name]={
            "numner":num,
            "email":email,
            "address":address
        }
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"contact '{name}' not found.")

def delete_contacts():
    name=input("Enter the contact name to delete:")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully:")
    else:
        print(f"Contact '{name}' not found.")


print("Welcome to the contact manager!")
pw=input("Enter the password to access your contacts:")
if pw=="1234":
    print("Correct password! Access granted.")
    while True:
        print("-- Contact Manager --")
        print("1. Add Contacts")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contacts")
        print("5. Delete contacts")
        print("6. Exit")

        choice=input("Enter your choice (1-6):")

        if choice=='1':
            add_contacts()
        elif choice=='2':
            view_saved_contacts()
        elif choice=='3':
            search_contacts()
        elif choice=='4':
            update_contacts()
        elif choice=='5':
            delete_contacts()
        elif choice=='6':
            print("Goodbye!")
            break
        else:
            print("Invaled choice. please enter a number between 1 and 5.")
else:
    print("Access denied: Incorrect password.")

