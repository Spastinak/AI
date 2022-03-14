

from boardView import clear, message, print_board, printWinner
from gameController import playerFinishCheck, shiftStones

board = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
#board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] # test board
playing = True

playerOne = True

messageCode = 0

player = "player1"
extraTurn = False


        
while(playing):
    clear()

    message(playerOne, messageCode)
    messageCode = 0

    print_board(board)
    
    
    userInput = input("Enter a letter to choose a bin or enter 'QUIT' to quit the game: ")

    # TODO find a better way to do this
    # why is there no switch case in python?
    chosenPit = 0 
    if userInput == "QUIT":
        playing = False
    elif playerOne and userInput == "a":
        chosenPit = 5
    elif playerOne and userInput == "b":
        chosenPit = 4
    elif playerOne and userInput == "c":
        chosenPit = 3
    elif playerOne and userInput == "d":
        chosenPit = 2
    elif playerOne and userInput == "e":
        chosenPit = 1
    elif playerOne and userInput == "f":
        chosenPit = 0
    elif not(playerOne) and userInput == "a":
        chosenPit = 7
    elif not(playerOne) and userInput == "b":
        chosenPit = 8
    elif not(playerOne) and userInput == "c":
        chosenPit = 9
    elif not(playerOne) and userInput == "d":
        chosenPit = 10
    elif not(playerOne) and userInput == "e":
        chosenPit = 11
    elif not(playerOne) and userInput == "f":
        chosenPit = 12
    else:
        chosenPit = -2
        messageCode = -2 # invaliad input
   
    # TODO add a if statement to check if messagecode = -2
    
    extraTurn, board = shiftStones(chosenPit, player, board)
    
    if playerFinishCheck(board):
        # TODO add methode to update the board as empty.
        break ## someone won the game
    
    if not(extraTurn):
        if player == "player1":
            player = "player2"
            playerOne = False
        else:
            player = "player1"
            playerOne = True

# end of while loop

printWinner(board)