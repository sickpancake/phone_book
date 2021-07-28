#create the phonebook class

import modules.ContactModule as ContactModule
class PhoneBook:
    def __init__(self):
        self.list = list()

    def getContacts(self):
        return self.list

    def getContact(self, name):
        pn = self.list.get(name, None)

        if (pn == None):
            return None

        contact = ContactModule.Contact(name, pn)
        return contact
 
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
        self.list.append(name + ": " + phoneNumber)
        print("added")

    def updateConact(self, contact):
        name = contact.getName()
        phoneNumber = contact.getPhoneNumber()
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
        self.list[name] = name + ": " + phoneNumber
        print("changed")

    def deleteContact(self, contact):
        name = contact.getName()
        if name in self.dict:
            deleteOrNot = input("Are you sure you want to delete " + name + " from contacts?")
            if deleteOrNot == "yes":
                print("deleting...")
                self.list.remove(name) 
            else:
                print("ok, not deleting")
        else:
            print("this contact is not in contacts")
            print("look!")
            print(self.dict )