'''Contact class'''
# create the Contact class


class Contact:
    '''create the contact class'''
    def __init__(self, name: str, phonenumber: str):
        self.name = name
        self.phonenumber = phonenumber

    def set_phone_number(self, phonenumber: str) -> None:
        """set an phonenumber"""
        self.phonenumber = phonenumber

    def get_phone_number(self) -> str:
        """get the phonenumber"""
        return self.phonenumber

    def set_name(self, name: str) -> None:
        """set the name"""
        self.name = name

    def get_name(self) -> str:
        """get the name"""
        return self.name
