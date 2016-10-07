def readfile():
    file = open("name.txt", "r")
    t = file.read()
    l = t.split("\n")
    short = set(l)
    size = len(short)
    print("There are %d names in the list" % size)
    print("The names are: " + ", ".join(short))





