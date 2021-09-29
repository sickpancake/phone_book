# create the phonebook class


from modules.ContactModule import Contact


class PhoneBook:
    def __init__(self):
        self.list = list()

    def getContacts(self) -> list:
        """get the contacts of this list"""
        return self.list

    def getContactsByName(self, name: str) -> list:
        """get an contact by it's name"""
        if (name == None):
            return None

        return [contact for contact in self.list if contact.name == name]

    def getFirstContact(self, name: str) -> Contact:
        """get the first contact of a name"""
        if (name == None):
            return None

        contact = [contact for contact in self.list if contact.name == name]

        return contact[0]

    def getContactsByNameAndOrder(self, name: str, order: int) -> list:
        """get an contact by there name and there order"""
        return self.getContactsByName(name)[order - 1]

    def matchingExisting(self, contact: Contact) -> Contact:
        """see if there is an contact in the phonebook that have the same properties"""
        for c in self.getContacts():
            rightPhoneNumber = c.getPhoneNumber() == contact.getPhoneNumber()
            rightName = c.getName() == contact.getName()
            if rightPhoneNumber and rightName:
                return True

        return False

    def validatePhoneNumber(self, phoneNumber: str) -> str:
        """check if the number has the right conditions"""
        if(len(phoneNumber) != 10):
            print("has to be 10 digits")
            return False

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            return False

        return True  

    def saveContact(self, contact: Contact) -> None:
        """Save a contact to phonebook"""

        # 1) return if there is already a contact with same name and phone number
        if self.matchingExisting(contact):
            return

        # 2) validate phone number
        if not self.validatePhoneNumber(contact.getPhoneNumber()):
            return

        # 3) add contact to list
        print("adding...")
        self.list.append(contact)
        print("added")

    def deleteContact(self, contact: Contact, order: int) -> None:
        """delete an contact"""
        if contact in self.getContacts():
            self.list.pop(order - 1)
        else:
            print("this contact is not in contacts")
            print("look!")
