from IO import *
from Board import *
import sys
import heapq
import random

class Agent:
    board: Board
    io: IO

    def __init__(self):
        self.board = Board()
        self.io = IO("DefinitelyARobot")

maximumDepth = 4
branchingFactor = 14


def numberOfBrokenThrees(state: Board, turn: int):
    pieceList: list
    numberOfBrokenThrees = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][
                piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][
                piece.col - 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] != -1:
                break

            if counter == 3:
                numberOfBrokenThrees += 1

        # up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                    piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
                break
            elif (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            elif (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] != -1:
                break

            if counter == 3:
                numberOfBrokenThrees += 1

        # diag left to right, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][
                piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][
                piece.col + 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] != -1:
                break

            if counter == 3:
                numberOfBrokenThrees += 1

        # left to right
        counter = 0
        for i in range(piece.col, piece.col + 4):

            if not ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                    piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
                break
            elif i <= 14 and state.board[piece.row][i] == turn:
                counter += 1
            elif i <= 14 and state.board[piece.row][i] != -1:
                break

            if counter == 3:
                numberOfBrokenThrees += 1

    return numberOfBrokenThrees

def numberOfOpenTwos(state: Board, turn: int):
    pieceList: list
    numberOfOpenTwos = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (
                piece.row - 2 >= 0 and piece.col - 2 >= 0 and state.board[piece.row - 2][piece.col - 2] == -1)):
            for i in range(2):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 2:
                    numberOfOpenTwos += 1

        # up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                piece.row - 2 >= 0 and state.board[piece.row - 2][piece.col] == -1)):
            for i in range(2):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 2:
                    numberOfOpenTwos += 1

        # diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (
                piece.row - 2 >= 0 and piece.col + 2 <= 14 and state.board[piece.row - 2][piece.col + 2] == -1)):
            for i in range(2):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 2:
                    numberOfOpenTwos += 1

        # left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                piece.col + 2 <= 14 and state.board[piece.row][piece.col + 2] == -1)):
            for i in range(piece.col, piece.col + 2):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 2:
                    numberOfOpenTwos += 1

    return numberOfOpenTwos


def numberOfThrees(state: Board, turn: int):
    pieceList: list
    numberOfThrees = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (
                piece.row - 3 >= 0 and piece.col - 3 >= 0 and state.board[piece.row - 3][piece.col - 3] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThrees += 1

        # up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                piece.row - 3 >= 0 and state.board[piece.row - 3][piece.col] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThrees += 1

        # diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (
                piece.row - 3 >= 0 and piece.col + 3 <= 14 and state.board[piece.row - 3][piece.col + 3] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThrees += 1

        # left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                piece.col + 3 <= 14 and state.board[piece.row][piece.col + 3] == -1)):
            for i in range(piece.col, piece.col + 3):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThrees += 1

    return numberOfThrees


def numberOfStraightFours(state: Board, turn: int):
    pieceList: list
    numberOfStraightFours = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (
                piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFours += 1

        # up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFours += 1

        # diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (
                piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFours += 1

        # left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
            for i in range(piece.col, piece.col + 4):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFours += 1

    return numberOfStraightFours


def numberOfFours(state: Board, turn: int):
    pieceList: list
    numberOfFours = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) ^ (
                piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFours += 1

        # up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) ^ (
                piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFours += 1

        # diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) ^ (
                piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFours += 1

        # left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) ^ (
                piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
            for i in range(piece.col, piece.col + 4):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFours += 1

    return numberOfFours

def numberOfBrokenFours(state: Board, turn: int):
    pieceList: list
    numberOfBrokenFours = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        # diag right to left, up
        counter = 0
        for i in range(5):

            if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] != -1:
                break

            if counter == 4:
                numberOfBrokenFours += 1

        # up
        counter = 0
        for i in range(5):

            if (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            elif (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] != -1:
                break

            if counter == 4:
                numberOfBrokenFours += 1

        # diag left to right, up
        counter = 0
        for i in range(5):

            if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] != -1:
                break

            if counter == 4:
                numberOfBrokenFours += 1

        # left to right
        counter = 0
        for i in range(piece.col, piece.col + 5):

            if i <= 14 and state.board[piece.row][i] == turn:
                counter += 1
            elif i <= 14 and state.board[piece.row][i] != -1:
                break

            if counter == 4:
                numberOfBrokenFours += 1

    return numberOfBrokenFours
    

def winningCondition(state: Board, turn: int):
    pieceList: list
    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces
                                      
    for piece in pieceList:
        #down
        counter = 0
        for i in range(piece.row, piece.row + 5):
            if i <= 14 and state.board[i][piece.col] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #up
        counter = 0
        for i in reversed(range(piece.row - 4, piece.row + 1)):
            if i >= 0 and state.board[i][piece.col] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #right to left
        counter = 0
        for i in reversed(range(piece.col - 4, piece.col + 1)):
            if i >= 0 and state.board[piece.row][i] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #left to right
        counter = 0
        for i in range(piece.col, piece.col + 5):
            if i <= 14 and state.board[piece.row][i] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #diag right to left, up
        counter = 0
        for i in range(5):
            if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #diag left to right up
        counter = 0
        for i in range(5):
            if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1
            
    return 0

def possibleMoves(state: Board, turn: int, depth: int):
    moveSetEarly = {}
    moveSetLater = []

    if state.turnNumber > 5 and depth < maximumDepth - 1:
        h = []
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.col+2):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        loc = Location(i, j)
                        state.putPiece(loc, turn)
                        value = utility(state)

                        if turn == 0:
                            value = -value

                        #If there is a winning move, only choose it
                        if value == -sys.maxsize and turn == 0:
                            onlyValue = [Location(i, j)]
                            return onlyValue

                        heapq.heappush(h, (value, Location(i, j)))
                        state.putPiece(loc, -1)

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.col+2):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        loc = Location(i, j)
                        state.putPiece(loc, turn)
                        value = utility(state)

                        if turn == 0:
                            value = -value

                        #If there is a winning move, only choose it
                        if value == -sys.maxsize and turn == 0:
                            onlyValue = [Location(i, j)]
                            return onlyValue
                            
                        heapq.heappush(h, (value, Location(i, j)))
                        state.putPiece(loc, -1)

        while len(moveSetLater) < branchingFactor:
            if not h:
                break
            else:
                move = heapq.heappop(h)[1]
                if move not in moveSetLater:
                    moveSetLater.append(move)

        return moveSetLater

    elif state.turnNumber > 2:
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.col+2):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        moveSetEarly[Location(i, j)] = 1

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.col+2):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        moveSetEarly[Location(i, j)] = 1
    else:
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-2, piece.row+3):
                for j in range(piece.col-2, piece.col+3):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        moveSetEarly[Location(i, j)] = 1

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-2, piece.row+3):
                for j in range(piece.col-2, piece.col+3):
                    if i >= 0 and i <= 14 and j >= 0 and j <= 14 and state.board[i][j] == -1:
                        moveSetEarly[Location(i, j)] = 1

    return moveSetEarly.keys()

def utility(state: Board):
    value = 0
    
    value += numberOfFours(state, 0) * 10
    value += numberOfStraightFours(state, 0) * 20
    value += numberOfThrees(state, 0) * 2
    value += numberOfBrokenThrees(state, 0) * 4
    value += numberOfBrokenFours(state, 0) * 10
    value += numberOfOpenTwos(state, 0)

    value -= numberOfFours(state, 1) * 20
    value -= numberOfStraightFours(state, 1) * 40
    value -= numberOfThrees(state, 1) * 4
    value -= numberOfBrokenThrees(state, 1) * 8
    value -= numberOfBrokenFours(state, 1) * 20
    value -= numberOfOpenTwos(state, 1) * 2

    agentWin = winningCondition(state, 0)
    opponentWin = winningCondition(state, 1)

    if agentWin:
        value = sys.maxsize

    elif opponentWin:
        value = -sys.maxsize
        
    return value
    
    
def minValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 0) or depth == maximumDepth:
        return utility(state)

    value = sys.maxsize

    for location in possibleMoves(state, 1, depth):
        state.putPiece(location, 1)
        value = min(value, maxValue(state, alpha, beta, depth + 1))
        state.putPiece(location, -1)
        if value <= alpha:
            return value
        beta = min(beta, value)

    return value
    

def maxValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 1) or depth == maximumDepth:
        return utility(state)

    value = -sys.maxsize

    for location in possibleMoves(state, 0, depth):
        state.putPiece(location, 0)
        value = max(value, minValue(state, alpha, beta, depth + 1))
        state.putPiece(location, -1)
        if value >= beta:
            return value
        alpha = max(alpha, value)
        
    return value

def alphabetaSearch(state: Board):

    bestActionValue = -sys.maxsize
    bestAction = -1
    
    for location in possibleMoves(state, 0, 1):

        state.putPiece(location, 0)

        if bestAction == -1:
            bestAction = location
        
        newValue = minValue(state, -sys.maxsize, sys.maxsize, 2)
        state.putPiece(location, -1)

        #If moves have the same value, pick a random one
        if newValue == bestActionValue:
            if(random.randrange(0,2) == 0):
                bestAction = location
                bestActionValue = newValue
            
        if newValue > bestActionValue:
            bestAction = location
            bestActionValue = newValue

    print("value: " + str(bestActionValue))

    return bestAction

agent = Agent()

while not game_over():
    while agent.io.ready():
        rd = read_move()
        move = -1
        print("Turn: " + str(agent.board.turnNumber))

        #Not the first move of the game
        if not rd == -1:
            print("row: " + str(rd.row) + ", col: " + str(rd.col))

            #dynamic so that it does not run out of time
            if agent.board.turnNumber == 40:
                maximumDepth = 3
                branchingFactor = 25
                print("updated branching factor")

            elif agent.board.turnNumber == 65:
                branchingFactor = 20

            elif agent.board.turnNumber == 150:
                branchingFactor = 15
            
            #someone swaps with us
            if agent.board.turnNumber == 1 and agent.board.board[rd.row][rd.col] == 0:
                agent.board.putPiece(rd)   

            agent.board.putPiece(rd, 1)

            #always start in the center
            if agent.board.turnNumber == 2:
                move = Location(7,7)
                
            else:
                move = alphabetaSearch(agent.board)

        #First move of the game
        else:
            move = Location(7,7)

        poss = possibleMoves(agent.board, 0, 1)
        agent.board.printBoard(poss)
    
        agent.io.write_move(move)
        agent.board.putPiece(move, 0)
        while agent.io.ready():
            pass
