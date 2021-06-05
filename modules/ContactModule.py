#create the Contact class
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
