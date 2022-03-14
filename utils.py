

def shiftStones(bin, player, board):
    
    boardCopy = board.copy() # copy board for safty
    # define player bins
    player1Bin = [0, 1, 2, 3, 4, 5]
    player2Bin = [12, 11, 10, 9, 8, 7] #[7, 8, 9, 10, 11, 12] maybe this list needs to be reversed
    
    extraTurn = False
    availableBins = 0 
    if player == "player1":
        availableBins = player1Bin
    else:
        availableBins = player2Bin
    
    stonesNumber = boardCopy[bin]
    boardCopy[bin] = 0
    
    for x in range(stonesNumber):
        bin += 1
        if bin > 13:
            bin = 0
            
        if ( (player == "player1" and bin == 13) or (player == "player2" and bin == 6)):
            bin += 1
        boardCopy[bin] += 1
    
    if (boardCopy[bin] == 1) and (bin in availableBins):
        if player == "player1":
            boardCopy[6] += boardCopy[bin]
            boardCopy[bin] = 0
            
            oppositeIndex = player1Bin.index(bin)
            oppositeBinNumber = player2Bin[oppositeIndex]
            boardCopy[6] += boardCopy[oppositeBinNumber]
            boardCopy[oppositeBinNumber] = 0
        
        else: 
            boardCopy[0] += boardCopy[bin]
            boardCopy[bin] = 0
            
            oppositeIndex = player2Bin.index(bin)
            oppositeBinNumber = player1Bin[oppositeIndex]
            boardCopy[13] += boardCopy[oppositeBinNumber]
            boardCopy[oppositeBinNumber] = 0
        
    if ( bin == 6 and player == "player1") or (bin == 13 and player == "player2"):
        extraTurn = True
        
    return boardCopy # TODO add extraTurn later

# TODO make a check if the player finishes or if there is an extra turn
def playerFinishCheck(board):
    
    bins = [[0, 1, 2, 3, 4, 5],[12, 11, 10, 9, 8, 7]]
    for binsList in bins:
        sum = 0
        for x in binsList:
            if board[x] == 6:
                sum += 1
        if sum == 6:
            return True
    return False