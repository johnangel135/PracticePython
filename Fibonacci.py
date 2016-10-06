def nhapso():
    so = str(input("Input number: "))
    while not so.isdecimal():
        so = str(input("Input number: "))
    so = int(so)
    return so
def F():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a +b
def run():
    a = nhapso()
    b =[]
    for index, i in enumerate(F()):
        if i > a: break
        b.append(i)
    print(b)