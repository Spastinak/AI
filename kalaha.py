

from boardView import clear, message, print_board, printWinner
from gameController import endBoard, playerFinishCheck, playerInput, shiftStones

board = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
#board = [0,0,0,0,0,1,0,0,0,0,0,12,0,0] # test board
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
    chosenPit, messageCode, playing = playerInput(userInput, player, messageCode, playing)
   
    if not(messageCode == -2) or not(playing):
        extraTurn, board = shiftStones(chosenPit, player, board)
        
        # someone won the game
        if playerFinishCheck(board): 
            endBoard(player, board)
            playing = False
        
        if not(extraTurn):
            if player == "player1":
                player = "player2"
                playerOne = False
            else:
                player = "player1"
                playerOne = True

# end of while loop

printWinner(board)