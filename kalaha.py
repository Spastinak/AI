

from boardView import clear, message, print_board, printWinner
from gameController import endBoard, playerFinishCheck, playerInput, shiftStones

board = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
#board = [0,0,0,0,0,1,0,0,0,0,0,12,0,0] # test board
playing = True
messageCode = 0

player = "player1"
extraTurn = False


        
while(playing):
    clear()

    message(player, messageCode)
    messageCode = 0

    print_board(board)
    
    
    userInput = input("Enter a letter to choose a bin or enter 'QUIT' to quit the game: ")
    chosenPit, messageCode, playing = playerInput(userInput, player, messageCode, playing)
   
    if not(messageCode == -2) or not(playing):
        extraTurn, board, messageCode = shiftStones(chosenPit, player, board, messageCode)
        if not(messageCode == -1):
            # someone won the game
            if playerFinishCheck(board):
                endBoard(player, board)
                playing = False
            
            if not(extraTurn):
                if player == "player1":
                    player = "player2"
                else:
                    player = "player1"

# end of while loop

printWinner(board)