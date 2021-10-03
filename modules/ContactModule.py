# create the Contact class


class Contact:
    def __init__(self, name: str, phoneNumber: str):
        self.name = name
        self.phoneNumber = phoneNumber

    def set_phone_number(self, phoneNumber: str) -> None:
        """set an phonenumber"""
        self.phoneNumber = phoneNumber

    def get_phone_number(self) -> str:
        """get the phonenumber"""
        return self.phoneNumber

    def set_name(self, name: str) -> None:
        """set the name"""
        self.name = name

    def get_name(self) -> str:
        """get the name"""
        return self.name
