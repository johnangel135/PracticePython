def checkT3(list):
    player1 = [1, 1, 1]
    player2 = [2, 2, 2]
    draw = 0
    diag1 = []
    diag2 = []

    for i in range(3):
        col = [row[i] for row in list]
        diag1.append(list[i][i])
        diag2.append(list[i][2 - i])
        if (player1 == list[i]) or (player1 == col):
            print("Player 1 win")
            break
        elif (player2 == list[i]) or (player2 == col):
            print("Player 2 win")
            break
        else:
            draw += 1

    if draw == 3:
        if (player1 == diag1) or (player1 == diag2):
            print("Player 1 win")
        elif (player2 == diag1) or (player2 == diag2):
            print("Player 2 win")
        else:
            print("Draw")
