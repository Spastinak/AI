

from boardView import clear, message, print_board
from utils import shiftStones


binAmount = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]

playing = True

playerOne = True

messageCode = 0

player = "player1"


        
while(playing):
    clear()

    message(playerOne, messageCode)
    messageCode = 0

    print_board(binAmount)
    
    
    userInput = input("Enter a letter to choose a bin or enter 'QUIT' to quit the game: ")

    # why is there no switch case in python?
    chosenBin = 0 
    if userInput == "QUIT":
        playing = False
    elif playerOne and userInput == "a":
        chosenBin = 5
    elif playerOne and userInput == "b":
        chosenBin = 4
    elif playerOne and userInput == "c":
        chosenBin = 3
    elif playerOne and userInput == "d":
        chosenBin = 2
    elif playerOne and userInput == "e":
        chosenBin = 1
    elif playerOne and userInput == "f":
        chosenBin = 0
    elif not(playerOne) and userInput == "a":
        chosenBin = 7
    elif not(playerOne) and userInput == "b":
        chosenBin = 8
    elif not(playerOne) and userInput == "c":
        chosenBin = 9
    elif not(playerOne) and userInput == "d":
        chosenBin = 10
    elif not(playerOne) and userInput == "e":
        chosenBin = 11
    elif not(playerOne) and userInput == "f":
        chosenBin = 12
    else:
        chosenBin = -2
        messageCode = -2 # invaliad input
   

    binAmount = shiftStones(chosenBin, player, binAmount)
    
    if player == "player1":
        player = "player2"
        playerOne = False
    else:
        player = "player1"
        playerOne = True

# end of while loop