import json

def save_contacts(manager, filename = "contacts.json"):
    contacts = []

    current = manager.head

    while current is not None:
        contact = {
            "name": current.name,
            "phone": current.phone,
            "email": current.email,
            "occupation": current.occupation,
            "is_fav": current.is_fav
        }

        contacts.append(contact)

        current = current.next

    with open(filename, "w") as file:
        json.dump(contacts, file, indent = 4)

def load_contacts(manager, filename = "contacts.json"):
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        return

    for contact in contacts:
        manager.add_contact(
            contact["name"],
            contact["phone"],
            contact["email"],
            contact["occupation"],
            contact["is_fav"]
        )