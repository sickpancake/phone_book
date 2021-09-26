# create the Contact class


class Contact:
    def __init__(self, name: str, phoneNumber: str):
        self.name = name
        self.phoneNumber = phoneNumber

    def setPhoneNumber(self, phoneNumber: str):
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name
