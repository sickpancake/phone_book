'''phonebook module'''
# import contact class

import os
import pathlib
import sqlite3

from modules.ContactModule import Contact


class PhoneBook:
    '''create phonebook class'''

    def __init__(self) -> None:
        # get a consistent path to database across operating systems
        # e.g.
        # Windows: 'C:\\Users\\wangy\\phonebook.db'
        # Linux:   '/home/wxh/phonebook.db'
        self.dbpath = os.path.join(pathlib.Path.home(), "phonebook.db")
        print('database is saved at: ' + self.dbpath)

        self.connection = sqlite3.connect(self.dbpath)
        self.cursor = self.connection.cursor()
        self.initialize()

    def __del__(self):
        print('closing database')
        self.connection.close()

    def initialize(self):
        '''initilize the database'''
        self.cursor.execute(
            '''
            create table if not exists phonebook
            (
                id integer primary key,
                name text,
                phonenumber text
            )
            '''
        )

        self.connection.commit()

    def get_contacts(self) -> list[Contact]:
        """get the contacts of this list"""

        # create an empty contact list first
        contact_list = list[Contact]()

        # select all contacts from phonebook
        results = self.cursor.execute('select * from phonebook')

        for each_row in results:
            # get contact name and phonenumber from this row
            name = each_row[1]
            phonenumber = each_row[2]
            contact_id = each_row[0]

            # assemble name and phonenumber into a contact
            contact = Contact(contact_id, name, phonenumber)

            # add the assembled contact into the list
            contact_list.append(contact)

        # return the list
        return contact_list

    def get_contacts_by_name(self, name: str) -> list[Contact]:
        '''get the contacts who has a certain name'''

        # create an empty contact list first
        contact_list = list[Contact]()

        for each_row in self.cursor.execute(
            '''
            select * from phonebook where name = :name
            ''',
            {
                "name": name
            }
        ):
            # get contact name and phonenumber from this row
            contact_id = each_row[0]
            contact_name = each_row[1]
            contact_phonenumber = each_row[2]

            # assemble id, name and phonenumber into a contact
            contact = Contact(contact_id, contact_name, contact_phonenumber)

            # add the assembled contact into the list
            contact_list.append(contact)

        # return list
        return contact_list

    def get_contacts_by_name_and_order(self, name: str, order: int) -> list[Contact]:
        '''get a contact by a name and a order'''
        contacts_by_name = self.get_contacts_by_name(name)
        contacts_by_name_at_order = contacts_by_name[order - 1]
        contacts = []
        contacts.append(contacts_by_name_at_order)
        return contacts

    def get_contacts_by_id(self, contact_id: int) -> Contact:
        '''get a contact whose id is the one inputed'''
        row = self.cursor.execute(
            '''
            select * from phonebook where id = :id
            ''',
            {
                'id': contact_id
            }
        )

        row = row.fetchall()
        row = row[0]
        contact_id = row[0]
        contact_name = row[1]
        contact_phonenumber = row[2]

        contact = Contact(contact_id, contact_name, contact_phonenumber)

        return contact

    def create_id(self) -> int:
        '''create the next possible id'''
        if not len(self.get_contacts()) == 0:
            new_id = len(self.get_contacts()) + 1

        else:
            new_id = 1

        return new_id

    def matching_existing(self, contact: Contact) -> None:
        '''check if there is aready a contact with the same properties'''
        # get the contact's name and phonenumber
        contact_phonenumber = contact.get_phone_number()
        contact_name = contact.get_name()

        # loop through all the rows
        for each_row in self.cursor.execute(
            '''
            select * from phonebook
            '''
        ):

            # see if that contact have the same phonenumber as the one that was inputed
            same_phonenumber = each_row[2] == contact_phonenumber
            # see if that contact have the same name as the one that was inputed
            same_name = each_row[1] == contact_name

            # if both true return true
            if same_phonenumber is True and same_name is True:
                return True

        # after looking through all the contacts and still none, return flase
        return False

    def validate_phone_number(self, phonenumber: str) -> bool:
        """check if the number has the right conditions"""

        # see if the phonenumber is all numbers
        try:
            int(phonenumber)
        except ValueError:
            print("number only")
            return False

            # check if the phonenumber has 10 digits
        if len(phonenumber) != 10:
            print("has to be 10 digits")
            return False

        return True

    def save_contact(self, contact: Contact) -> None:
        '''save a contact to the database'''

        # reutrn if there's already a contact with the same properties
        if self.matching_existing(contact) is True:
            return

        # validate phonenumber
        if not self.validate_phone_number(contact.get_phone_number()):
            return

        # add contact to database
        print("adding...")
        self.cursor.execute(
            '''
            insert into phonebook values (null, :name, :phonenumber)
            ''',
            {
                "name": contact.get_name(),
                "phonenumber": contact.get_phone_number()
            }
        )

        self.connection.commit()
        print("added")

    def delete_contact(self, contact: Contact, contact_id: int):
        '''delete a contact from the database'''
        if contact is None:
            return

        if len(self.get_contacts()) < contact_id:
            return

        self.cursor.execute(
            '''
            delete from phonebook where id = :id
            ''',
            {
                'id': contact_id
            }
        )

        self.connection.commit()

    def delete_all_contacts_by_name(self, name: str) -> None:
        '''delete all contacts named whose name is the one that was inputed'''
        self.cursor.execute(
            '''
            delete from phonebook where name = :name
            ''',
            {
                "name": name
            }
        )

        self.connection.commit()
