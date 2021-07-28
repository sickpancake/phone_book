import unittest

from modules import PhoneBookModule
from modules import ContactModule

class PhoneBookModuleTest(unittest.TestCase):

    def test_default_phonebook_should_be_empty(self):
        phoneBook = PhoneBookModule.PhoneBook()
        
        expected = 0
        actual = len(phoneBook.getContacts())

        self.assertEqual(expected, actual)

    def test_add_contact(self):
        phoneBook = PhoneBookModule.PhoneBook()

        expectedContact = ContactModule.Contact("A", "0123456789")
        phoneBook.saveContact(expectedContact)

        actualContact = phoneBook.getContact("A")

        self.assertEqual(expectedContact.name, actualContact.name)
        self.assertEqual(expectedContact.phoneNumber, actualContact.phoneNumber)