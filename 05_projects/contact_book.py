def display_menu():
    print("\n==== CONTACT BOOK ====")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")



def view_contacts(contacts):
    if not contacts:
            print("No contacts found.")
            return 
    
    print("\n---- Contacts ----")
        
    for name, phone in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print()


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10



def add_contact(contacts):

    name = input("Enter your name:").strip().capitalize()
    
    if not name:
        print("Name cannot be empty.")
        return
    
    if name in contacts:
        print("Contact already exists.")
        return
    
    while True:
        phone = input("Enter your phone number:").strip()
        
        if is_valid_phone(phone):
            break
        
        print("Invalid phone number. Enter exactly 10 digits.")
        
        # if not phone:
        #     print("Phone number cannot be empty.")
        #     return
        
        # if not is_valid_phone(phone):
        #     print("Invalid phone number. Enter exactly 10 digits.")
        #     return
        
    contacts[name] = phone
    save_contacts(contacts)
        
    print("Contact added successfully.")

    

def search_contact(contacts):
    name = input("Enter contact name:").strip()
    
    if not name:
        print("Name cannot be empty.")
        return
    
    phone = contacts.get(name)

    if phone:
        print("\nContact Found")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter contact name to update:").strip()
    
    if not name:
        print("Name cannot be empty.")
        return
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    print(f"Current Phone: {contacts[name]}")
    
    new_phone = input("Enter new phone number:").strip()
    
    if not new_phone:
        print("Phone number cannot be empty.")
        return
    
    if not is_valid_phone(new_phone):
            print("Invalid phone number. Enter exactly 10 digits.")
            return
        
    contacts[name] =new_phone
    save_contacts(contacts)
    
    print("Contact updated successfully.")



def delete_contact(contacts):
    name = input("Enter contact name to delete:").strip()
    
    if not name:
        print("Name cannot be empty.")
        return
    
    if name not in contacts:
        print("Contact not found.")
        return
    
    contacts.pop(name)
    save_contacts(contacts)
    
    print("Contact deleted successfully.")



def save_contacts(contacts):
    with open("contact.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}, {phone}\n")



def load_contacts():
    contacts = {}
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
                
    except FileNotFoundError:
        pass
        
    return contacts



def main():
    contacts = load_contacts()
    
    while True:
        display_menu()
        
        choice = input("Choose an option:").strip()
        
        if choice == "1":
            view_contacts(contacts)
            
        elif choice == "2":
            add_contact(contacts)
            
        elif choice == "3":
            search_contact(contacts)
        
        elif choice == "4":
            update_contact(contacts)
            
        elif choice == "5":
            delete_contact(contacts)
            
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
    
        else:
            print("Invalid choice. Please try again.")


main()