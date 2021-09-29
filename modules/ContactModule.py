# create the Contact class


class Contact:
    def __init__(self, name: str, phoneNumber: str):
        self.name = name
        self.phoneNumber = phoneNumber

    def setPhoneNumber(self, phoneNumber: str) -> None:
        """set an phonenumber"""
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self) -> str:
        """get the phonenumber"""
        return self.phoneNumber

    def setName(self, name: str) -> None:
        """set the name"""
        self.name = name

    def getName(self) -> str:
        """get the name"""
        return self.name
