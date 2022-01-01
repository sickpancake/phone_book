'''main program'''
# import the classes
from modules.ContactModule import Contact
from modules.phonebook_module_two import PhoneBook


def print_list(list_of_objects: list[Contact]) -> None:
    """print a list"""
    for contact in list_of_objects:
        print(str(contact.contact_id) + ": "
        + contact.name + ": "
        + contact.phonenumber)

def create_from_input(person_name: str, phone_number: str, phonebook: PhoneBook) -> None:
    '''
    create from input
    '''
    contact = Contact(phonebook.create_id(), person_name, phone_number)

    phonebook.save_contact(contact)

    print_list(phonebook.get_contacts())

def delete_from_input(contact_id: str, phonebook: PhoneBook):
    '''
    delete from input
    '''
    contact_id = int(contact_id)
    contact = phonebook.get_contacts_by_id(contact_id)

    if contact is None:
        print("contact does not exist")
        return

    phonebook.delete_contact(contact, contact_id)

    list_phonenumbers = phonebook.get_contacts()

    if len(list_phonenumbers) == 1 or len(list_phonenumbers) > 1:
        print_list(phonebook.get_contacts())

    else:
        print("there are no contacts in phonebook now")

if __name__ == "__main__":

    phone_book = PhoneBook()

    # main loop
    while True:
        CMD_PART_A = "You can read, create and delete. "
        CMD_PART_B = "If you don't want to use the code anymore, "
        CMD_PART_C = "you can type 'quit' or 'exit'. "
        CMD_PART_D = "What do you want to do? "
        cmd = input(CMD_PART_A + CMD_PART_B + CMD_PART_C + CMD_PART_D)

        if cmd == "read":
            print_list(phone_book.get_contacts())

        if cmd == "create":
            p = input("person's name? ")
            pn = input("phone number? ")
            create_from_input(p, pn, phone_book)

        if cmd == "delete":
            cid = input("id? ")
            delete_from_input(cid, phone_book)

        if cmd in ['exit', 'quit']:
            break
