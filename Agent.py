from IO import *
from Board import *
import copy
import sys

class Agent:
    board: Board
    io: IO

    def __init__(self):
        board = Board()
        io = IO("DefinitelyNotARobot")

maximum depth = 12
def numberOfBrokenThrees(state: Board):

def numberOfThrees(state: Board):

def numberOfStraightFours(state: Board):

def numberOfFours(state: Board):

def winningCondition(state: Board):
    for piece in agentPlacedPieces:

        #up
        counter = 0
        for i in range(piece.x, piece.x + 5):
            if i <= 14 and state.board[i][piece.y] == 0:
                counter += 1
            else:
                break
            
            if counter == 5:
                return True

        #down
        counter = 0
        for i in reversed(range(piece.x - 4, piece.x + 1)):
            if i >= 0 and state.board[i][piece.y] == 0:
                counter += 1
            else break;
            
            if counter == 5:
                return True

        #left to right
        counter = 0
        for i in reversed(range(piece.y - 4, piece.y + 1)):
            if i >= 0 and state.board[piece.x][i] == 0:
                counter += 1
            else break;
            
            if counter == 5:
                return True

        #right to left
        counter = 0
        for i in range(piece.y, piece.y + 5)):
            if i <= 14 and state.board[piece.x][i] == 0:
                counter += 1
            else break;
            
            if counter == 5:
                return True

        #diag right to left, up
        counter = 0
        for i in range(5):
            if piece.x - i >= 0 and piece.y - i >= 0 and state.board[piece.x - i][piece.y - i] == 0:
                counter += 1
            else break;
            
            if counter == 5:
                return True

        #diag left to right up
        counter = 0
        for i in range(5):
            if piece.x - i >= 0 and piece.y + i <= 14 and state.board[piece.x - i][piece.y + i] == 0:
                counter += 1
            else break;
            
            if counter == 5:
                return True

def possibleMoves(state: Board):
    moveSet: list
    for i in range(15):
        for j in range(15):
            if state.board[i][j] == -1:
                moveSet.append(Location(i, j))

    return moveSet

#NEEDS CHANGES
def utility(state: Board):
    value = 0;
    value += numberOfFours(state) * 100
    value += numberOfStraightFours(state) * 1000
    value += numberOfThrees(state) * 50
    value += numberOfBrokenThrees(state) * 25
    if hasDoubleThreat(state):
        value += 10000

    return value
    
    
def minValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state) or depth == maximumDepth:
        return utility(state)

    value = sys.maxsize

    newState = copy.copy(state)
    newState.putPiece(location, 0)
    
    for location in possibleMoves(state):
        value = min(value, maxValue(newState, alpha, beta))
        if alpha <= beta:
            return value
        beta = min(beta, value)

    return value
    

def maxValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state) or depth == maximumDepth:
        return utility(state):

    value = -sys.maxsize

    newState = copy.copy(state)
    newState.putPiece(location, 1)

    for location in possibleMoves(state):
        value = max(value, minValue(newState, alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)
        
    return value

def alphabetaSearch(state: Board):

    bestActionValue = -sys.maxsize
    bestAction = -1
    
    for location in possibleMoves(state):

        if(bestAction == -1) bestAction = location
        
        newValue = maxValue(result(state, action), -sys.maxsize, sys.maxsize)
        if(newValue > bestActionValue):
            bestAction = action
            bestActionValue = newValue

    return bestAction

agent = Agent()

while(agent.ready()):
    agent.board.putPiece(IO.read_move())
    move = alphabetaSearch(agent.board.board)
    IO.write_move(move)



    

