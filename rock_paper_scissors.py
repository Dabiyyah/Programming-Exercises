
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?\n")
    if player == computer:
        print("Tie!\n")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!\n", computer, "covers", player)
        else:
            print("You win!\n", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!\n", computer, "cut", player)
        else:
            print("You win!\n", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...\n", computer, "smashes", player)
        else:
            print("You win!\n", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!\n")
    #player was set to True, but we want it to be False so the loop continues

    player = input("Would you like to play again?\n")
    if player == "Yes":
        player = False
        computer = t[randint(0,2)]
    else:
        exit()
