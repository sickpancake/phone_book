import unittest

from modules.phonebook_module_two import PhoneBook
from modules.ContactModule import Contact


class PhoneBookModuleTest(unittest.TestCase):
    def setUp(self):
        phoneBook = PhoneBook()
        phoneBook.cursor.execute(
            'drop table phonebook'
        )

    def test_default_phonebook_should_be_empty(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        expected = 0
        actual = len(phoneBook.get_contacts())

        self.assertEqual(expected, actual)

    def test_add_contact(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()
        
        expectedContact = Contact(phoneBook.create_id(),"A", "0123456789")
        phoneBook.save_contact(expectedContact)

        actualContact = phoneBook.get_contacts_by_name("A")[0]


        self.assertEqual(expectedContact.name, actualContact.name)
        self.assertEqual(expectedContact.phonenumber,
                         actualContact.phonenumber)

    def test_allow_duplicate(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        contact1 = Contact(phoneBook.create_id(), "A", "1234567890")
        contact2 = Contact(phoneBook.create_id(), "A", "0987654321")

        phoneBook.save_contact(contact1)
        phoneBook.save_contact(contact2)

        self.assertEqual(2, len(phoneBook.get_contacts()))

    def test_id_should_be_numbers(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        contact = Contact(phoneBook.create_id, "A", "1234567890")
        self.assertEqual(contact.name, "A", "contact name is not A")
        self.assertEqual(contact.phonenumber, "1234567890",
                         "contact phone number is not 1234567890")
        phoneBook.save_contact(contact)
        self.assertEqual(len(phoneBook.get_contacts()), 1,
                         "there should be 1 contact in phone book")

        raised = False
        try:
            phoneBook.delete_contact(phoneBook.get_contacts_by_id(1), "1")
        except TypeError():
            raised = True

        self.assertEqual(raised, False)

    def test_delete_all_contacts_named_A(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))
        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phoneBook.get_contacts()))
        phoneBook.delete_all_contacts_by_name("A")
        self.assertEqual(0, len(phoneBook.get_contacts()))

    def test_delete_second_contact_named_A(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))
        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phoneBook.get_contacts()))

        contact = phoneBook.get_contacts_by_id(2)

        phoneBook.delete_contact(contact, 2)
        self.assertEqual(len(phoneBook.get_contacts()), 1)
        with self.assertRaises(IndexError):
            phoneBook.get_contacts_by_id(2)

    def test_delete_first_contact_named_A(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))
        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phoneBook.get_contacts()))

        contact = phoneBook.get_contacts_by_id(1)

        phoneBook.delete_contact(contact, 1)
        self.assertEqual(len(phoneBook.get_contacts()), 1)
        with self.assertRaises(IndexError):
            phoneBook.get_contacts_by_id(1)

    def test_no_duplicate_contact(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))

        self.assertEqual(1, len(phoneBook.get_contacts()))

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))

        self.assertEqual(1, len(phoneBook.get_contacts()))

    def test_matchingExisting_negative(self):
        phoneBook = PhoneBook()
        phoneBook.initialize()

        phoneBook.save_contact(Contact(phoneBook.create_id(), "A", "1234567890"))
        self.assertEqual(len(phoneBook.get_contacts()), 1)
        phoneBook.save_contact(Contact(phoneBook.create_id(), "B", "0987654321"))
        self.assertEqual(len(phoneBook.get_contacts()), 2)

        contact = Contact(phoneBook.create_id(), "c", "0987654321")

        self.assertEqual(phoneBook.matching_existing(contact), False)
