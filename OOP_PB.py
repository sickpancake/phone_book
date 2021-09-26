#import the classes
from typing import List
from modules.ContactModule import Contact 
from modules.PhoneBookModule import PhoneBook

if __name__ == "__main__":

    phoneBook = PhoneBook()


def print_list(list: List[Contact]):
    for contact in list:
        print(contact.name + ": " + contact.phoneNumber)
    

#main loop
while True:
    cmdpartA = "You can read, create and delete. "
    cmdpartB = "If you don't want to use the code anymore, "
    cmdpartC = "you can type 'quit' or 'exit'. "
    cmdpartD =  "What do you want to do? "
    cmd = input(cmdpartA + cmdpartB + cmdpartC + cmdpartD)
    if(cmd=="read"):
        print_list(phoneBook.getContacts())

    if(cmd=="create"):
        p = input("person's name? ")
        pn = input("phone number? ")
        
        contact = Contact(p, pn)
        phoneBook.saveContact(contact)

        print_list(phoneBook.getContacts())

    if(cmd=="delete"):
        pn = input("name? ")
        order = input("order? ")
        contact = phoneBook.getContactsByNameAndOrder(pn, order)
        
        if (contact == None):
            print("contact does not exist")
            continue
        
        phoneBook.deleteContact(contact, order)

        list = phoneBook.getContacts()
        
        if len(list) == 1:
            print_list(phoneBook.getContacts())

        else:
            print("there are no contacts in phonebook now")

    if(cmd=="quit" or cmd=="exit"):
        break
