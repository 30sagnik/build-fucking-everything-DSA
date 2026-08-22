class ContactNode:

    def __init__(self, name, phone, email, occupation, is_fav = False):
        self.name = name
        self.phone = phone
        self.email = email
        self.occupation = occupation
        self.is_fav = is_fav
        self.next = None
        