'''
this test suite targets logics in phonebook module
'''

import unittest

from modules.phonebook_module import PhoneBook
from modules.contact_module import Contact


class PhoneBookModuleTest(unittest.TestCase):
    '''
    test suite
    '''

    def setUp(self):
        phonebook = PhoneBook()
        phonebook.cursor.execute(
            'drop table phonebook'
        )

    def test_default_phonebook_should_be_empty(self):
        '''check if a new phonebook is empty'''
        phonebook = PhoneBook()
        phonebook.initialize()

        expected = 0
        actual = len(phonebook.get_contacts())

        self.assertEqual(expected, actual)

    def test_add_contact(self):
        '''test if you can add a contact'''
        phonebook = PhoneBook()
        phonebook.initialize()

        expected_contact = Contact(phonebook.create_id(), "A", "0123456789")
        phonebook.save_contact(expected_contact)

        actual_contact = phonebook.get_contacts_by_name("A")[0]

        self.assertEqual(expected_contact.name, actual_contact.name)
        self.assertEqual(expected_contact.phonenumber,
                         actual_contact.phonenumber)

    def test_allow_duplicate(self):
        '''check if the database allow duplicates'''
        phonebook = PhoneBook()
        phonebook.initialize()

        contact1 = Contact(phonebook.create_id(), "A", "1234567890")
        contact2 = Contact(phonebook.create_id(), "A", "0987654321")

        phonebook.save_contact(contact1)
        phonebook.save_contact(contact2)

        self.assertEqual(2, len(phonebook.get_contacts()))

    def test_delete_all_contacts_named_a(self):
        '''check if the delete all contacts by name function works'''
        phonebook = PhoneBook()
        phonebook.initialize()

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))
        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phonebook.get_contacts()))
        phonebook.delete_all_contacts_by_name("A")
        self.assertEqual(0, len(phonebook.get_contacts()))

    def test_delete_second_contact_named_a(self):
        '''try delete the second contact name a'''
        phonebook = PhoneBook()
        phonebook.initialize()

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))
        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phonebook.get_contacts()))

        contact = phonebook.get_contacts_by_id(2)

        phonebook.delete_contact(contact, 2)
        self.assertEqual(len(phonebook.get_contacts()), 1)

        contact = phonebook.get_contacts_by_id(2)
        self.assertIsNone(contact)

    def test_delete_first_contact_named_a(self):
        '''try delete the first contact name a'''
        phonebook = PhoneBook()
        phonebook.initialize()

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))
        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "0987654321"))

        self.assertEqual(2, len(phonebook.get_contacts()))

        contact = phonebook.get_contacts_by_id(1)

        phonebook.delete_contact(contact, 1)
        self.assertEqual(len(phonebook.get_contacts()), 1)
        contact = phonebook.get_contacts_by_id(1)
        self.assertIsNone(contact)

    def test_no_duplicate_contact(self):
        '''try to add a contact with the same properties should not work'''
        phonebook = PhoneBook()
        phonebook.initialize()

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))

        self.assertEqual(1, len(phonebook.get_contacts()))

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))

        self.assertEqual(1, len(phonebook.get_contacts()))

    def test_matching_existing_negative(self):
        '''try to add a contact that doesn't have the same properties should work'''

        phonebook = PhoneBook()
        phonebook.initialize()

        phonebook.save_contact(
            Contact(phonebook.create_id(), "A", "1234567890"))
        self.assertEqual(len(phonebook.get_contacts()), 1)
        phonebook.save_contact(
            Contact(phonebook.create_id(), "B", "0987654321"))
        self.assertEqual(len(phonebook.get_contacts()), 2)

        contact = Contact(phonebook.create_id(), "c", "0987654321")

        self.assertEqual(phonebook.matching_existing(contact), False)
