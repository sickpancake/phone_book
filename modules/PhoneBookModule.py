#create the phonebook class
class PhoneBook:
    def __init__(self):
        self.dict = {

        }

    def getContacts(self):
        return self.dict

    def getContact(self, name):
        pn = self.dict.get(name, None)

        if (pn == None):
            return None

        contact = Contact(name, pn)
        return contact

    def saveContact(self, contact):
        name = contact.getName()
        phoneNumber = contact.getPhoneNumber()
        if(len(phoneNumber) == 10):
            print("first check done!")

        else:
            print("has to be 10 digits")
            exit()

        if name in self.dict:
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
        self.dict[name] = phoneNumber
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
        self.dict[name] = phoneNumber
        print("changed")

    def deleteContact(self, contact):
        name = contact.getName()
        if name in self.dict:
            deleteOrNot = input("Are you sure you want to delete " + name + " from contacts?")
            if deleteOrNot == "yes":
                print("deleting...")
                self.dict.pop(name) 
            else:
                print("ok, not deleting")
        else:
            print("this contact is not in contacts")
            print("look!")
            print(self.dict )