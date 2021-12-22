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
        self.dbpath =  os.path.join(pathlib.Path.home(), "phonebook.db")
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
