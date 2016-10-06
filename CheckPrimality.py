import math
def nhapso():
    c = str(input("Please input a number: "))
    while not c.isdecimal():
        c = str(input("Please input a number: "))
    c = int(c)
    return c
def startgame():
    so = nhapso()
    a = [x for x in range(2,so) if so % x == 0]
    if len(a) == 0: print("This is prime")
    else: print("Not prime")
