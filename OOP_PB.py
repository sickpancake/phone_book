# import the classes
from typing import List
from modules.ContactModule import Contact
from modules.PhoneBookModule import PhoneBook


if __name__ == "__main__":

    phone_book = PhoneBook()


def print_list(list: List[Contact]) -> None:
    """print a list"""
    for contact in list:
        print(contact.name + ": " + contact.phoneNumber)


# main loop
while True:
    cmd_part_a = "You can read, create and delete. "
    cmd_part_b = "If you don't want to use the code anymore, "
    cmd_part_c = "you can type 'quit' or 'exit'. "
    cmdpartD = "What do you want to do? "
    cmd = input(cmd_part_a + cmd_part_b + cmd_part_c + cmdpartD)
    if(cmd == "read"):
        print_list(phone_book.get_contacts())

    if(cmd == "create"):
        p = input("person's name? ")
        pn = input("phone number? ")

        contact = Contact(p, pn)
        phone_book.save_contact(contact)

        print_list(phone_book.get_contacts())

    if(cmd == "delete"):
        pn = input("name? ")
        order = input("order? ")
        contact = phone_book.get_contacts_by_name_and_order(pn, order)

        if (contact == None):
            print("contact does not exist")
            continue

        phone_book.delete_contact(contact, order)

        list = phone_book.get_contacts()

        if len(list) == 1:
            print_list(phone_book.get_contacts())

        else:
            print("there are no contacts in phonebook now")

    if(cmd == "quit" or cmd == "exit"):
        break
