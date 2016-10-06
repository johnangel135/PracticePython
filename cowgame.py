import random
from random import  randint

def guess(num):

    cows = 0
    bulls = 0
    a = randint(1000,9999)
    print ('the right answer is: ', a)

    for index, i in enumerate(num):
        if str(a)[index] ==  i :
            cows += 1
        else:
            bulls += 1

    print ("cows : %r and bulls : %r" %(cows,bulls))

def startgame():
    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")
    b = (input("please input ur guess: "))
    guess(b)



