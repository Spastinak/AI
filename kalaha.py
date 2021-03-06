

from webbrowser import get
from boardView import clear, message, print_board, printWinner
from gameController import endBoard, nextplayer, goalTest, playerInput, shiftStones
from minimax import getBestMove

board = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
#board = [0,0,0,0,0,1,0,0,0,0,0,12,0,0] # test board
playing = True
messageCode = 0

player = "player2"
extraTurn = False

        
while(playing):
    clear()

    message(player, messageCode)
    messageCode = 0

    print_board(board)

    if (player == "player2"):
        bestMove = getBestMove(board)
        extraTurn, board, messageCode = shiftStones(bestMove, player, board, messageCode)
        if (player != extraTurn):
            player = nextplayer(player)

        if (messageCode == 1):
            clear()
            print_board(board)
            playing = False   
            
    else:
        userInput = input("Enter a letter to choose a pit or enter 'QUIT' to quit the game: ")
        chosenPit, messageCode, playing = playerInput(userInput, player, messageCode, playing)
        if (not(messageCode == -2) or not(playing)):
            extraTurn, board, messageCode = shiftStones(chosenPit, player, board, messageCode)
            if (player != extraTurn):
                player = nextplayer(player)
            if (messageCode == 1):
                clear()
                print_board(board)
                playing = False
    
    
# end of while loop

printWinner(board)