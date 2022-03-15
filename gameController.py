
# TODO add check if selected pit is empty
def shiftStones(pit, player, board):
    
    boardCopy = board.copy() # copy board for safty
    # define player bins
    player1Pits = [0, 1, 2, 3, 4, 5]
    player2Pits = [12, 11, 10, 9, 8, 7] #[7, 8, 9, 10, 11, 12] maybe this list needs to be reversed
    
    extraTurn = False
    availablePits = 0 
    if player == "player1":
        availablePits = player1Pits
    else:
        availablePits = player2Pits
    
    stonesNumber = boardCopy[pit]
    boardCopy[pit] = 0
    
    for x in range(stonesNumber):
        pit += 1
        if pit > 13:
            pit = 0
            
        if ( (player == "player1" and pit == 13) or (player == "player2" and pit == 6)):
            pit += 1
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
        
    return extraTurn, boardCopy

# check if either of the two board side pits are empty 
def playerFinishCheck(board):
    
    pits = [[0, 1, 2, 3, 4, 5],[12, 11, 10, 9, 8, 7]]
    for pitList in pits:
        sum = 0
        for x in pitList:
            if board[x] == 0:
                sum += 1
        if sum == 6:
            return True
    return False

def endBoard(player, board):
    player1Pits = [0, 1, 2, 3, 4, 5]
    player2Pits = [12, 11, 10, 9, 8, 7]
    if player == "player1":
        for x in player2Pits:
            board[13] += board[x]
            board[x] = 0
    if player == "player2":
        for x in player1Pits:
            board[6] += board[x]
            board[x] = 0