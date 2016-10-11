def drawSquare():
    def print_square():
        print(" --- " * board_size + "\n" + "|    " * (board_size + 1))

    if __name__ != "__main__":
        board_size = int(input("What size of game board? "))

        for index in range(board_size):
            print_square()


def drawnotSquare():
    def print_line():
        print(" --- " * row)

    def print_row():
        print("|    " * (row + 1))

    if __name__ != "__main__":
        line = int(input("What line of game board? "))
        row = int(input("What row of game board? "))

        for index in range(line):
            print_line()
            print_row()
        print_line()
