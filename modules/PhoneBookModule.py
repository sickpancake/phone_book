'''phonebook module'''
# create the phonebook class


from modules.ContactModule import Contact


class PhoneBook:
    """create phonebook class"""
    def __init__(self):
        self.list = list()

    def get_contacts(self) -> list:
        """get the contacts of this list"""
        return self.list

    def get_contacts_by_name(self, name: str) -> list:
        """get an contact by it's name"""
        if name is None:
            return None

        return [contact for contact in self.list if contact.name == name]

    def get_first_contact(self, name: str) -> Contact:
        """get the first contact of a name"""
        if name is None:
            return None

        contact = [contact for contact in self.list if contact.name == name]

        return contact[0]

    def get_contacts_by_name_and_order(self, name: str, order: int) -> list:
        """get an contact by there name and there order"""
        return self.get_contacts_by_name(name)[order - 1]

    def matching_existing(self, contact: Contact) -> Contact:
        """see if there's an contact in the phonebook that have the same properties"""
        for c in self.get_contacts():
            right_phonenumber = c.get_phone_number() == contact.get_phone_number()
            right_name = c.get_name() == contact.get_name()
            if right_phonenumber and right_name:
                return True

        return False

    def validate_phone_number(self, phoneNumber: str) -> str:
        """check if the number has the right conditions"""
        if len(phoneNumber) != 10:
            print("has to be 10 digits")
            return False

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            return False

        return True

    def save_contact(self, contact: Contact) -> None:
        """Save a contact to phonebook"""

        # 1) return if there's already a contact with same propaties
        if self.matching_existing(contact):
            return

        # 2) validate phone number
        if not self.validate_phone_number(contact.get_phone_number()):
            return

        # 3) add contact to list
        print("adding...")
        self.list.append(contact)
        print("added")

    def delete_contact(self, contact: Contact, order: int) -> None:
        """delete an contact"""
        if contact in self.get_contacts():
            self.list.pop(order - 1)
        else:
            print("this contact is not in contacts")
            print("look!")
            