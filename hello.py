from random import randint
num_1 = int(input("choose a number for your range"))
num_2 = int(input("choose another"))
e = "yes"
num_range=(randint(num_1, num_2))
while e == "yes":
    user_num=int(input("choose a number from the two numbers you chose for the range(ex. 1-10)"))

    if num_range == user_num:
        print("you win")
        e="no"

    else:
        print("you lose")
        e="no"


    if user_num>num_range:
        print ("too big")
        e="no"

    elif user_num<num_range:
        print ("too small")
        e="no"

    else:
        print ("nice job")
        e="no"


