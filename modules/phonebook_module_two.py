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

            # assemble name and phonenumber into a contact
            contact = Contact(name, phonenumber)

            # add the assembled contact into the list
            contact_list.append(contact)

        # return the list
        return contact_list
