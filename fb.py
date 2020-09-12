

def print_dict(d):
    print(d)
    print(len(d))

tb_dict = {
    
}

while True:
    cmd = input("what do you want to do? ")

    if(cmd=="read"):
        print_dict(tb_dict)

    if(cmd=="create"):
        tb_dict[input("person's name? ")] = input("phone number? ")
        print_dict(tb_dict)

    if(cmd=="update"):
        tb_dict[input("person's name? ")] = input("phone number? ")
        print_dict(tb_dict)

    if(cmd=="delete"):
        tb_dict.pop(input("name? "))
        print_dict(tb_dict)

    if(cmd=="quit" or cmd=="exit"):
        break
