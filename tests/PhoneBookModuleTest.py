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

        actualContact = phoneBook.getFirstContact("A")

        self.assertEqual(expectedContact.name, actualContact.name)
        self.assertEqual(expectedContact.phoneNumber, actualContact.phoneNumber)

    def test_allow_duplicate(self):
        phoneBook = PhoneBookModule.PhoneBook()

        contact1 = ContactModule.Contact("A", "1234567890")
        contact2 = ContactModule.Contact("A", "0987654321")

        phoneBook.saveContact(contact1)
        phoneBook.saveContact(contact2)

        self.assertEqual(2, len(phoneBook.getContacts()))

    def test_order_should_be_numbers(self):
        phoneBook = PhoneBookModule.PhoneBook()

        contact = ContactModule.Contact("A", "1234567890")
        self.assertEqual(contact.name, "A", "contact name is not A")
        self.assertEqual(contact.phoneNumber, "1234567890", "contact phone number is not 1234567890")
        phoneBook.saveContact(contact)
        self.assertEqual(len(phoneBook), 1, "there is no contact in phone book")

        #tbc
        self.fail()
    
    def test_delete_all_contacts_named_A(self):
        phoneBook = PhoneBookModule.PhoneBook()

        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))
        phoneBook.saveContact(ContactModule.Contact("A", "0987654321"))

        self.assertEqual(2, len(phoneBook.getContacts()))

        
        
    def test_delete_second_contact_named_A(self):
        phoneBook = PhoneBookModule.PhoneBook()

        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))
        phoneBook.saveContact(ContactModule.Contact("A", "0987654321"))

        self.assertEqual(2, len(phoneBook.getContacts()))
        
        contact = phoneBook.getContactsByNameAndOrder("A", 2)
        
        phoneBook.deleteContact(contact, 2)
        self.assertEqual(len(phoneBook.list), 1)
        self.assertEqual(contact.phoneNumber, "0987654321")

    def test_delete_first_contact_named_A(self):
        phoneBook = PhoneBookModule.PhoneBook()

        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))
        phoneBook.saveContact(ContactModule.Contact("A", "0987654321"))

        self.assertEqual(2, len(phoneBook.getContacts()))
        
        contact = phoneBook.getContactsByNameAndOrder("A", 1)
        
        phoneBook.deleteContact(contact, 1)
        self.assertEqual(len(phoneBook.list), 1)
        self.assertEqual(contact.phoneNumber, "1234567890")


    def test_no_duplicate_contact(self):
        phoneBook = PhoneBookModule.PhoneBook()

        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))
        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))

        self.assertEqual(1, len(phoneBook.getContacts()))

    def test_update_contact(self):
        phoneBook = PhoneBookModule.PhoneBook()

        phoneBook.saveContact(ContactModule.Contact("A", "1234567890"))
        contactA = phoneBook.getContactsByNameAndOrder("A", 1)
        self.assertIsNotNone(contactA, "contact a should not be none")
        self.assertEqual(contactA.getName(), "A")
        self.assertEqual(contactA.getPhoneNumber(), "1234567890")
        
        phoneBook.updateConact(contactA, "1234567899")
        contactA = phoneBook.getContactsByNameAndOrder("A", 1)
        self.assertIsNotNone(contactA, "contact a should not be none")
        self.assertEqual(contactA.getName(), "A")
        self.assertEqual(contactA.getPhoneNumber(), "1234567899")
        
