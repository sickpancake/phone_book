'''
this test suite targets logics in main (i.e. phonebook.py)
'''
import unittest

from phonebook import create_from_input, delete_from_input
from modules.phonebook_module import PhoneBook


class PhoneBookTest(unittest.TestCase):
    '''
    test suite
    '''
    def test_create_and_delete_positive(self):
        """should raise TypeError when use a int as name"""
        phonebook = PhoneBook()
        create_from_input("jeif", "1234567890", phonebook)

        contact = phonebook.get_contacts_by_name("jeif")[0]

        delete_from_input(str(contact.get_contact_id()), phonebook)

        contact = phonebook.get_contacts_by_id(contact.get_contact_id())

        self.assertIsNone(contact)