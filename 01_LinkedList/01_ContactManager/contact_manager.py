from contact import ContactNode

class ContactManager:

    def __init__(self):
        #Creates an empty Linked List
        self.head = None

    def count_contact(self):
        total = 0
        current = self.head
        while current is not None:
            total +=1
            current = current.next
        return total

    def add_contact(self, name, phone, email, occupation, is_fav = False):
        #Create the new Contact
        new_contact = ContactNode(name, phone, email, occupation, is_fav)

        if self.head is None:
            self.head = new_contact
            print("Contact Saved.")
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_contact
        print("Contact Saved.")

    def display_contact(self):
        if self.head is None:
            print("No contacts found.")
            return
        
        current = self.head
        i = 1
        total_contacts = self.count_contact()
        print(f"\n------{total_contacts} Contacts------\n")
        while current is not None:
            fav = "FAV" if current.is_fav else ""
            print(f"\n {i}. Name : {current.name} | Phone : {current.phone} | Email : {current.email} | Occupation : {current.occupation} | {fav}")

            i += 1
            current = current.next

    def search_contact(self, search):
        current = self.head
        found = False
        i = 1
        print("\n------Contacts found------\n")
        while current is not None:
            if search.lower() in current.name.lower():
                fav = "FAV" if current.is_fav else ""
                print(f"\n {i}. Name : {current.name} | Phone : {current.phone} | Email : {current.email} | Occupation : {current.occupation} | {fav}")
                i += 1
                found = True
            current = current.next
        if not found:
            print("No contacts found according to your search..")

    def update_contact(self, search, name = None, phone = None, email = None, occupation = None):
        current = self.head

        while current is not None and search.lower() != current.name.lower():
            current = current.next

        if current is None:
            return False
        if name is not None:
            current.name = name
        if phone is not None:
            current.phone = phone
        if email is not None:
            current.email = email
        if occupation is not None:
            current.occupation = occupation
        print(f"Contact of {current.name} is updated!")
        return True

    def delete_contact(self, search):
        current = self.head
        if current is None:
            return False
        if current.name.lower() == search.lower():
            self.head = current.next
            print("Contact Deleted")
            return True
        while current.next is not None and current.next.name.lower() != search.lower():
            current = current.next
        if current.next is None:
            return False
        current.next = current.next.next
        print("Contact Deleted")
        return True

    def toggle_fav(self, search):
        current = self.head
        while current is not None and current.name.lower() != search.lower():
            current = current.next
        if current is None:
            return False
        current.is_fav = not current.is_fav
        return True

    def display_fav(self):
        current = self.head
        i = 0
        print("-------Favourites-------")
        while current is not None:
            if current.is_fav:
                i += 1
                fav = "FAV" if current.is_fav else ""
                print(f"\n {i}. Name : {current.name} | Phone : {current.phone} | Email : {current.email} | Occupation : {current.occupation} | {fav}")

            current = current.next
        if i == 0:
            print("No Favourite Contacts found.")

    def filter_occupation(self, occupation):
        current = self.head
        i = 0
        print(f"------{occupation}-------")
        while current is not None:
            if current.occupation.lower() == occupation.lower():
                i += 1
                fav = "FAV" if current.is_fav else ""
                print(f"\n {i}. Name : {current.name} | Phone : {current.phone} | Email : {current.email} | Occupation : {current.occupation} | {fav}")

            current = current.next
        if i == 0:
            print(f"No {occupation} found in Contact List.")



    