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

    def saveContact(self, contact):
        name = contact.getName()
        phoneNumber = contact.getPhoneNumber()
        if(len(phoneNumber) == 10):
            print("first check done!")

        else:
            print("has to be 10 numbers")
            exit()

        if name in self.dict:
            print("name is taken. look yourself!")
            print_dict(self.dict)
            exit()

        else:
            print("second check done")

        try:
            int(phoneNumber)
        except ValueError:
            print("number only")
            exit()

        self.dict[name] = phoneNumber