def print_dict(dict):
        print(dict)

class Contact:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

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

if __name__ == "__main__":

    phoneBook = PhoneBook()

while True:
    cmd = input("You can read, create, update and delete. If you don't want to use the code anymore, you can type 'quit' or 'exit'. What do you want to do? ")
    if(cmd=="read"):
        print_dict(phoneBook.getContacts())

    if(cmd=="create"):
        p = input("person's name? ")
        pn = input("phone number? ")
        
        contact = Contact(p, pn)
        phoneBook.saveContact(contact)

        print_dict(phoneBook.getContacts())


    if(cmd=="update"):
        pn2 = input("person's name? ")
        contact = phoneBook.getContact(pn2)
        if (contact == None):
            print("contact does not exist")
            continue

        phn2 = input("phone number? ")
        
        phoneBook.updateConact(contact)

        print_dict(phoneBook.getContacts())

    if(cmd=="delete"):
        pn = input("name? ")
        contact = phoneBook.getContact(pn)
        if (contact == None):
            print("contact does not exist")
            continue

        phoneBook.deleteContact(contact)

        print_dict(phoneBook.getContacts())

    if(cmd=="quit" or cmd=="exit"):
        break
