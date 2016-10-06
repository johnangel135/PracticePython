import random


def nhapso():
    so = str(input("Please input a number 1-9: "))
    while (not so.isdecimal()):
        so = str(input("Please input a number correctly 1-9: "))
    so = int(so)
    while (so < 1 or so > 9):
        so = str(input("Please input a number correctly 1-9: "))
        so = int(so)

    return so


def taoso():
    "This function generate random number"
    goal = random.randint(1, 9)
    return goal


def startgame():
    a = taoso()
    b = nhapso()
    c = 1
    while (a != b):
        if a < b:
            print("Input a lower number: ")
            b = nhapso()
            c += 1
            continue
        else:
            print("Input a higher number: ")
            b = nhapso()
            c += 1
            continue

    print("You win!!!!!!!!, you have try %d time(s)" % c)

