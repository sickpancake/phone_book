'''Contact class'''
# create the Contact class


class Contact:
    '''an object that contains a name and phonenumber'''
    def __init__(self, contact_id: int, name: str, phonenumber: str):
        self.name = name
        self.phonenumber = phonenumber
        self.contact_id = contact_id

    def get_contact_id(self) -> int:
        return self.contact_id
    
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


