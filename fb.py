

def print_dict(d):
    print(d)
    print(len(d))

tb_dict = {
    
}

while True:
    cmd = input("You can read, create, update and delete. If you don't want to use the code anymore, you can type 'quit' or 'exit'. What do you want to do? ")
    if(cmd=="read"):
        print_dict(tb_dict)

    if(cmd=="create"):

        tb_dict[ input("person's name? ")] = pn = input("phone number? ")
        try:
            int(pn)
        except ValueError:
            print ("number olny.")
            break

        print_dict(tb_dict)

    if(cmd=="update"):
        tb_dict[input("person's name? ")] = npn = input("phone number? ")
        try:
            int(npn)
        except ValueError:
            print("number olny.")
            break
        print_dict(tb_dict)

    if(cmd=="delete"):
        tb_dict.pop(input("name? "))
        print_dict(tb_dict)

    if(cmd=="quit" or cmd=="exit"):
        break
