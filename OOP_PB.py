#import the classes
from modules.ContactModule import Contact 
from modules.PhoneBookModule import PhoneBook

if __name__ == "__main__":

    phoneBook = PhoneBook()

#main loop
while True:
    cmd = input("You can read, create, update and delete. If you don't want to use the code anymore, you can type 'quit' or 'exit'. What do you want to do? ")
    if(cmd=="read"):
         for conact in phoneBook.list:
            print(conact.name + ': ' + conact.phoneNumber)

    if(cmd=="create"):
        p = input("person's name? ")
        pn = input("phone number? ")
        
        contact = Contact(p, pn)
        phoneBook.saveContact(contact)

        for conact in phoneBook.list:
            print(conact.name + ': ' + conact.phoneNumber)


    if(cmd=="update"):
        pn2 = input("person's name? ")
        contact = phoneBook.getContact(pn2)
        if (contact == None):
            print("contact does not exist")
            continue

        phn2 = input("phone number? ")
        
        phoneBook.updateConact(contact)

        for conact in phoneBook.list:
            print(conact.name + ': ' + conact.phoneNumber)

    if(cmd=="delete"):
        pn = input("name? ")
        contact = phoneBook.getContact(pn)
        
        if (contact == None):
            print("contact does not exist")
            continue
        
        phoneBook.deleteContact(contact)

        for conact in phoneBook.list:
            print(conact.name + ': ' + conact.phoneNumber)

    if(cmd=="quit" or cmd=="exit"):
        break
