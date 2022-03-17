

import sys
from boardView import message
from gameController import playerFinishCheck, shiftStones


player1Pits = [0, 1, 2, 3, 4, 5]
player2Pits = [12, 11, 10, 9, 8, 7]
        
def eval(board):
    player1stones = board[6]
    player2stones = board[13]  

    # for i in range(6):
    #     player1stones += board[i]
    #     player2stones += board[i+7]

    return player1stones-player2stones


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
            aiPlayer, boardCopy, messageCode = shiftStones(i,"player2", boardCopy, 0)
            evaluation = minimax(boardCopy, aiPlayer, 7, alpha, beta)
            if (evaluation > maxEval):
                maxEval = evaluation
                bestMove = i
    return bestMove

    
def minimax(board, aiPlayer, depth, alpha, beta):
    minint = -sys.maxsize - 1

    if (depth == 0 or playerFinishCheck(board)):
        evaluation = eval(board)
        return evaluation

    if (aiPlayer):
        maxEval = minint

        for i in player2Pits:
            if (not(board[i] == 0)):
                boardClone = board.copy()
                aiPlayer, boardCopy, messageCode = shiftStones(i,"player2", boardClone, 0)

                evaluation = minimax(boardClone, aiPlayer , depth-1, alpha, beta)

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
                aiPlayer, boardCopy, messageCode = shiftStones(i,"player1", boardClone, 0)

                evaluation = minimax(boardClone, aiPlayer , depth-1, alpha, beta)

                if (evaluation < minEval):
                    minEval = evaluation
                if (evaluation < beta):
                    beta = evaluation
                if (beta <= alpha):
                    break

        return minEval


