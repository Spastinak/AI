import os

# prints the board binAmount is the the array with every stone in it
def print_board(board):
    boardCopy = board.copy()
    pitAmount = convertBoard(boardCopy)
    
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ pitAmount[12] +" | "+ pitAmount[11] +" | "+ pitAmount[10] +" | "+ pitAmount[9] +" | "+ pitAmount[8] +" | "+ pitAmount[7] +" |    |")
    print("| "+ pitAmount[13] +" |----+----+----+----+----+----| "+ pitAmount[6] +" |")
    print("|    | "+ pitAmount[0] +" | "+ pitAmount[1] +" | "+ pitAmount[2] +" | "+ pitAmount[3] +" | "+ pitAmount[4] +" | "+ pitAmount[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("        f    e    d    c    b    a\n")


# used for clearing the terminal
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): # if computer is running windows use cls
        command = 'cls'
    os.system(command)
    
    
def message(player, messageCode):
    message = ""
    if player == "player1" and messageCode == 0:
        message = "\nYour turn.\n"
    elif player == "player2" and messageCode == 0:
        message = "\nAI is thinking...\n"
    elif messageCode == -2:
        message = "\ninvalid input. Try again.\n"
    elif messageCode == -1:
        message = "\nChoose a non-empty pit, you silly human.\n"
    print(message)
  
    
# convert the board to strings for use in print_Board
def convertBoard(pitAmount):
    i = 0
    # convert the binAmount to strings
    for element in pitAmount: 
        pitAmount[i] = int(pitAmount[i]) # remove extra spaces
        if int(pitAmount[i]) < 10:
            pitAmount[i] = " " + str(pitAmount[i]) # if binAmount is a single diget 
        else :
            pitAmount[i] = str(pitAmount[i]) # double diget
        i += 1
    # end of the for loop
    return pitAmount

def printWinner(board):
    clear()
    if (board[13] > board[6]):
        print("\nAI is the winner\n")
    elif (board[13] < board[6]):
        print("\nYou are the winner\n")
    else:
        print("\nDraw\n")
    print_board(board)