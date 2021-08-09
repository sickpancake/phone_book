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

    def test_allow_duplicate(self):
        phoneBook = PhoneBookModule.PhoneBook()

        contact1 = ContactModule.Contact("A", "1234567890")
        contact2 = ContactModule.Contact("A", "0987654321")

        phoneBook.saveContact(contact1)
        phoneBook.saveContact(contact2)

        self.assertEqual(2, len(phoneBook.getContacts()))

    def test_delete_contact(self):
        phoneBook = PhoneBookModule.PhoneBook()

        contact1 = ContactModule.Contact("A", "1234567890")

        phoneBook.saveContact(contact1)

        self.assertEqual(1, len(phoneBook.getContacts()))

        # to be completed...