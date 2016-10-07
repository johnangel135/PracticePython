import DecodeWeb
def wrtweb():
    data = DecodeWeb.decode()
    file = open("duong.txt", "w")
    file.write(data)
    file.close()
