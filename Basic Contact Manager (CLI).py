

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if contacts:
        print("Contacts list:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def main():
    while True:
        print("\nContact Manager Options:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
