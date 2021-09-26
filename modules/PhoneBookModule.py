# create the phonebook class


from modules.ContactModule import Contact


class PhoneBook:
    def __init__(self):
        self.list = list()

    def getContacts(self):
        return self.list

    def getContactsByName(self, name: str):
        if (name == None):
            return None

        return [contact for contact in self.list if contact.name == name]

    def getFirstContact(self, name: str):
        if (name == None):
            return None

        contact = [contact for contact in self.list if contact.name == name]

        return contact[0]

    def getContactsByNameAndOrder(self, name: str, order: int):
        return self.getContactsByName(name)[order - 1]

    def matchingExisting(self, contact: Contact):
        # todo - code here
        for c in self.getContacts():
            rightPhoneNumber = c.getPhoneNumber() == contact.getPhoneNumber()
            rightName = c.getName() == contact.getName()
            if rightPhoneNumber and rightName:
                return True

        return False

    def validatePhoneNumber(self, phoneNumber: str):
        # todo - code here
        if(len(phoneNumber) != 10):
            print("has to be 10 digits")
            return False

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            return False

        return True  # return properly later

    def saveContact(self, contact: Contact):
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

    def deleteContact(self, contact: Contact, order: int):
        if contact in self.getContacts():
            self.list.pop(order - 1)
        else:
            print("this contact is not in contacts")
            print("look!")
