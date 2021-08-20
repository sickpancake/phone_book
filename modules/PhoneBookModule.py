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

    def saveContact(self, contact):
        name = contact.getName()
        phoneNumber = contact.getPhoneNumber()
        if(len(phoneNumber) == 10):
            print("first check done!")

        else:
            print("has to be 10 digits")
            exit()

        if name in self.list:
            wantToDouble = input("do you want to double this name cause this name is taken?")
            print(self.dict)
            if wantToDouble == "yes":
                print("second check done!")

            else:
                print("not doubling")
                exit()

        else:
            print("second check done!")

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            exit()

        print("last check done!")
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
