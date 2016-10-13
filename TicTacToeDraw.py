import numpy as np

game = np.zeros((3, 3), dtype=np.int)
print(game)
check = True #True for player 1
element_process = lambda i: ("X" if i == 1 else ("O" if i == 2 else " "))

def printboard(board):
	print("\n game = [%s]\n" % ",\n\t\t ".join(["[%s]" % ", ".join(map(element_process, board[i])) for i in range(3)]))

def usermove(check):
    if check:
        tem = input("Player 1: Please input your move format row,col:")
    else:
        tem = input("Player 2: Please input your move format row,col:")
    move = tem.split(",")
    return move


def checkmove(player1_2):
    move = usermove(check)
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    while game[row][col] == 0:
        if player1_2:
            game[row][col] = "1"
        else:
            game[row][col] = "2"
        printboard(game)
        return not player1_2
