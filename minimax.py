

import sys
from boardView import message
from gameController import goalTest, shiftStones



player1Pits = [0, 1, 2, 3, 4, 5]
player2Pits = [12, 11, 10, 9, 8, 7]
        
def eval(board):

    player1points = board[6]*4
    player2points = board[13]*4
    for i in player1Pits:
        if board[i] == 13:
            player1points += 4
        elif board[i]+i == 6:
            player1points += 1
        elif board[i] == 0:
            player1points += 1

    for i in player2Pits:
        if board[i] == 13:
            player1points += 4
        elif board[i] + i == 13:
            player1points += 1
        elif board[i] == 0:
            player1points += 1


    # for i in range(6):
    #     player1stones += board[i]
    #     player2stones += board[i+7]
    #return player2stones-player1stones
    return player2points-player1points


def getBestMove(board):
    maxint = sys.maxsize
    minint = -sys.maxsize - 1

    bestMove = 0
    maxEval = minint
    alpha = minint
    beta = maxint

    
    for i in player2Pits:
        if (not(board[i] == 0)):
            boardCopy = board.copy()
            player, boardCopy, messageCode,  = shiftStones(i,"player2", boardCopy, 0)
            evaluation = minimax(boardCopy, player, 3, alpha, beta, )
            if (evaluation > maxEval):
                maxEval = evaluation
                bestMove = i
    
    
    return bestMove

    
def minimax(board, player, depth, alpha, beta ):
    minint = -sys.maxsize - 1

    if (depth == 0 or goalTest(board)):
        evaluation = eval(board)
        return evaluation

    if (player == "player2"):
        maxEval = minint

        for i in player2Pits:
            if (not(board[i] == 0)):
                boardClone = board.copy()
                player, boardClone, messageCode  = shiftStones(i,"player2", boardClone, 0)

                evaluation = minimax(boardClone, player , depth-1, alpha, beta, )

                if (evaluation > maxEval):
                    maxEval = evaluation
                if (evaluation > alpha):
                    alpha = evaluation
                if (beta <= alpha):
                    break

        return maxEval
    else:
        maxint = sys.maxsize

        minEval = maxint

        for i in player1Pits:
            if (not(board[i] == 0)):
                boardClone = board.copy()
                player, boardClone, messageCode = shiftStones(i,"player1", boardClone, 0)

                evaluation = minimax(boardClone, player , depth-1, alpha, beta)

                if (evaluation < minEval):
                    minEval = evaluation
                if (evaluation < beta):
                    beta = evaluation
                if (beta <= alpha):
                    break

        return minEval


