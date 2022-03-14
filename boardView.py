import os

# prints the board binAmount is the the array with every stone in it
def print_board(board):
    boardCopy = board.copy()
    binAmount = convertBoard(boardCopy)
    
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ binAmount[12] +" | "+ binAmount[11] +" | "+ binAmount[10] +" | "+ binAmount[9] +" | "+ binAmount[8] +" | "+ binAmount[7] +" |    |")
    print("| "+ binAmount[13] +" |----+----+----+----+----+----| "+ binAmount[6] +" |")
    print("|    | "+ binAmount[0] +" | "+ binAmount[1] +" | "+ binAmount[2] +" | "+ binAmount[3] +" | "+ binAmount[4] +" | "+ binAmount[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("        f    e    d    c    b    a\n")


# used for clearing the terminal
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): # if computer is running windows use cls
        command = 'cls'
    os.system(command)
    
    
def message(playerOne, messageCode):
    message = ""
    if playerOne and messageCode == 0:
        message = "\nPlayer one's turn.\n"
    elif not(playerOne) and messageCode == 0:
        message = "\nPlayer two's turn.\n"
    elif messageCode == -2:
        message = "\invalid input. Try again.\n"
    elif messageCode == -1:
        message = "\nChoose a non-empty bin idiot.\n"
    print(message)
  
    
# convert the board to strings for use in print_Board
def convertBoard(binAmount):
    i = 0
    # convert the binAmount to strings
    for element in binAmount: 
        binAmount[i] = int(binAmount[i]) # remove extra spaces
        if int(binAmount[i]) < 10:
            binAmount[i] = " " + str(binAmount[i]) # if binAmount is a single diget 
        else :
            binAmount[i] = str(binAmount[i]) # double diget
        i += 1
    # end of the for loop
    return binAmount