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
        p = input("person's name? ")
        pn = input("phone number? ")
        
        sipid = p in tb_dict
        if sipid==True:
            print("this name is unavailable")
            break

        tb_dict[(p)] = pn
        l = len(pn)

        if(l == 10):
            print("first check done")

       

        elif(l > 10):
            print("has to be 10 numbers")
            break

        else:
            print("10 numbers")
            break
            
        

        try:
            int(pn)
        except ValueError:
            print ("number olny.")
            break

        print_dict(tb_dict)



    

    if(cmd=="update"):
        pn2 = input("person's name? ")
        phn2 = input("phone number? ")
        tb_dict[pn2] = npn = phn2

        l2 = len(phn2)

        if(l2 == 10):
            print("first check done")

        elif(l2 > 11):
            print("has to be 10 numbers")
            break

        else:
            print("10 numbers")
            break

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
