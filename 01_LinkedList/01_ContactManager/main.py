from contact_manager import ContactManager
from storage import load_contacts, save_contacts

manager = ContactManager()
load_contacts(manager)

while True:
    print("\n========================CONTACT MANAGER========================\n")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Toggle Favourite")
    print("7. Display Favourites")
    print("8. Filter Occupation")
    print("9. Exit")

    choice = input("Enter your Choice[1-9]: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone No.: ")
        email = input("Email: ")
        occupation = input("Occupation: ")

        manager.add_contact(name, phone, email, occupation)

        save_contacts(manager)

    elif choice == "2":
        manager.display_contact()

    elif choice == "3":
        search = input("Enter Name to Search: ")
        manager.search_contact(search)

    elif choice == "4":
        search = input("Enter Contact to Update: ")
        name = input("New Name: ") or None
        phone = input("New Phone No.: ") or None
        email = input("New Email: ") or None
        occupation = input("New Occupation: ") or None
        manager.update_contact(search, name, phone, email, occupation)

        save_contacts(manager)

    elif choice == "5":
        search = input("Enter Contact to Delete: ")
        manager.delete_contact(search)

        save_contacts(manager)

    elif choice == "6":
        search = input("Enter Contact to toggle favourite: ")
        manager.toggle_fav(search)

        save_contacts(manager)

    elif choice == "7":
        manager.display_fav()

    elif choice == "8":
        occupation = input("Enter Occupation you want to look for: ")
        manager.filter_occupation(occupation)

    elif choice == "9":
        print("-----------------THANK YOU-----------------")
        break

    else:
        print("Invalid Choice")