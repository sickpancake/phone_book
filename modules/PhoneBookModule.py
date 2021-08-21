#create the phonebook class

import modules.ContactModule as ContactModule
class PhoneBook:
    def __init__(self):
        self.list = list()

    def getContacts(self):
        return self.list

    def getContactsByName(self, name):
        if (name == None):
            return None
    
        return [contact for contact in self.list if contact.name == name]
 
    def getFirstContact(self, name):
        if (name == None):
            return None
    
        contact = [contact for contact in self.list if contact.name == name]

        return contact[0]

    def getContactsByNameAndOrder(self, name, order):
        return self.getContactsByName(name)[int(order) - 1]

    def matchingExisting(self, contact):
        # todo - code here
        for c in self.getContacts():
            if c.getPhoneNumber() == contact.getPhoneNumber() and c.getName() == contact.getName():
                return True
            
        return False

    def validatePhoneNumber(self, phoneNumber):
        # todo - code here
        if(len(phoneNumber) != 10):
            print("has to be 10 digits")
            return False

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            return False

        return True # return properly later

    def saveContact(self, contact):
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

    def updateConact(self, contact, phoneNumber):
        if(len(phoneNumber) == 10):
            print("first check done!")
        else:
            print("has to be 10 digits")
            exit()

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            exit()
        
        print("last check done!")
        print("changing...")
        contact.setPhoneNumber(phoneNumber)
        print("changed")

    def deleteContact(self, contact, order):
        if contact in self.list:
                self.list.pop(int(order) - 1) 
        else:
            print("this contact is not in contacts")
            print("look!")
