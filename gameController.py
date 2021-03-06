
player1Pits = [0, 1, 2, 3, 4, 5]
player2Pits = [12, 11, 10, 9, 8, 7]

def shiftStones(pit, player, board, messageCode):
    
    boardCopy = board.copy() # copy board for safty
    # define player bins

    extraTurn = False
    availablePits = 0 
    if player == "player1":
        availablePits = player1Pits
    else:
        availablePits = player2Pits
    
    stonesNumber = boardCopy[pit]
    if not(stonesNumber == 0):
        boardCopy[pit] = 0
        
        for x in range(stonesNumber):
            pit += 1

            if ( (player == "player1" and pit == 13) or (player == "player2" and pit == 6)):
                pit += 1

            if pit > 13:
                pit = 0 
            
            boardCopy[pit] += 1
        
        if (boardCopy[pit] == 1) and (pit in availablePits):
            if player == "player1":
                boardCopy[6] += boardCopy[pit]
                boardCopy[pit] = 0
                
                oppositeIndex = player1Pits.index(pit)
                oppositePitNumber = player2Pits[oppositeIndex]
                boardCopy[6] += boardCopy[oppositePitNumber]
                boardCopy[oppositePitNumber] = 0
            
            else: 
                boardCopy[0] += boardCopy[pit]
                boardCopy[pit] = 0
                
                oppositeIndex = player2Pits.index(pit)
                oppositePitNumber = player1Pits[oppositeIndex]
                boardCopy[13] += boardCopy[oppositePitNumber]
                boardCopy[oppositePitNumber] = 0
            
        if ( pit == 6 and player == "player1") or (pit == 13 and player == "player2"):
            extraTurn = True
            
        if goalTest(boardCopy):
            boardCopy = endBoard(boardCopy)
            messageCode = 1

        if (player == "player1" and not(extraTurn)):
            player = "player2"
        elif( player == "player2" and not(extraTurn)):
            player = "player1"
        elif(player == "player1" and extraTurn):
            player = "player1"
        else:
            player = "player2"       

        return player, boardCopy, messageCode
    else:
        messageCode = -1
        return player, boardCopy, messageCode

# check if either of the two board side pits are empty 
def goalTest(board):
    
    pits = [player1Pits,player2Pits]
    for pitList in pits:
        sum = 0
        for x in pitList:
            if board[x] == 0:
                sum += 1
        if sum == 6:
            return True
    return False

def endBoard(board):
    boardCopy = board.copy()
    for x in player2Pits:
        boardCopy[13] += boardCopy[x]
        boardCopy[x] = 0

    for x in player1Pits:
        boardCopy[6] += boardCopy[x]
        boardCopy[x] = 0
    return boardCopy
            
def playerInput(userInput, player, messageCode, playing):
    chosenPit = 0 
    if userInput == "QUIT":
        playing = False
    elif player == "player1" and userInput == "a":
        chosenPit = 5
    elif player == "player1" and userInput == "b":
        chosenPit = 4
    elif player == "player1" and userInput == "c":
        chosenPit = 3
    elif player == "player1" and userInput == "d":
        chosenPit = 2
    elif player == "player1" and userInput == "e":
        chosenPit = 1
    elif player == "player1" and userInput == "f":
        chosenPit = 0
    else:
        chosenPit = -2
        messageCode = -2 # invaliad input
    return chosenPit, messageCode, playing

def nextplayer(player):
    if (player == "player1"):
        player = "player2"
    else:
        player = "player1"
    return player