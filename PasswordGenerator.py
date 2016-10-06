import random
import string

def sizeofpassword():
    size = random.randint(10,20)
    return size

def pwgenerate():
    size = sizeofpassword()
    p = []
    while size >0:
        p.append(random.choice(string.printable))
        size -= 1
    return p


def checkpw():
    checkok = True
    while checkok:
        p = pwgenerate()
        upper = set(p).intersection(string.ascii_uppercase)
        lower = set(p).intersection(string.ascii_lowercase)
        digit = set(p).intersection(string.digits)
        spect = set(p).intersection(string.punctuation)
        space = set(p).intersection(string.whitespace)
        if (not upper) or (not lower) or (not digit) or (not spect) or space:
            checkok = True
        else:
            checkok = False
    print("".join(p))








