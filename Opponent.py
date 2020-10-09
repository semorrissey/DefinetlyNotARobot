from IO import *
from Board import *
import sys
import heapq

class Agent:
    board: Board
    io: IO

    def __init__(self):
        self.board = Board()
        self.io = IO("DefinitelyARobot")

maximumDepth = 2
def numberOfBrokenThrees(state: Board, turn: int):
    pieceList: list
    numberOfBrokenThreesCounter = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        #diag right to left, up
        counter = 0
        for i in range(4):            

            if not ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] != -1:
                break

            if counter == 3:
                numberOfBrokenThreesCounter += 1
        
        #up
        counter = 0
        for i in range(4):
            
            if not ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
                break
            elif (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            elif (piece.row - i) >= 0 and state.board[piece.row - i][piece.col] != -1:
                break

            if counter == 3:
                numberOfBrokenThreesCounter += 1

        #diag left to right, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] != -1:
                break

            if counter == 3:
                numberOfBrokenThreesCounter += 1

        #left to right
        counter = 0
        for i in range(piece.col, piece.col + 4):

            if not ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
                break
            elif i <= 14 and state.board[piece.row][i] == turn:
                counter += 1
            elif i <= 14 and state.board[piece.row][i] != -1:
                break

            if counter == 3:
                numberOfBrokenThreesCounter += 1

    return numberOfBrokenThreesCounter

def numberOfThrees(state: Board, turn: int):
    pieceList: list
    numberOfThreesCounter = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        #diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThreesCounter += 1
        
        #up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (piece.row - 3 >= 0 and state.board[piece.row - 3][piece.col] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThreesCounter += 1

        #diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
            for i in range(3):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThreesCounter += 1

        #left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
            for i in range(piece.col, piece.col + 3):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 3:
                    numberOfThreesCounter += 1

    return numberOfThreesCounter

def numberOfStraightFours(state: Board, turn: int):
    pieceList: list
    numberOfStraightFoursCounter = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        #diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFoursCounter += 1
        
        #up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFoursCounter += 1

        #diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFoursCounter += 1

        #left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
            for i in range(piece.col, piece.col + 4):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfStraightFoursCounter += 1

    return numberOfStraightFoursCounter

def numberOfFours(state: Board, turn: int):
    pieceList: list
    numberOfFoursCounter = 0

    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces

    for piece in pieceList:
        #diag right to left, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][piece.col + 1] == -1) ^ (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][piece.col - 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFoursCounter += 1
        
        #up
        counter = 0
        if ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) ^ (piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFoursCounter += 1

        #diag left to right, up
        counter = 0
        if ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) ^ (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
            for i in range(4):
                if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFoursCounter += 1

        #left to right
        counter = 0
        if ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) ^ (piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
            for i in range(piece.col, piece.col + 4):
                if i <= 14 and state.board[piece.row][i] == turn:
                    counter += 1
                else:
                    break

                if counter == 4:
                    numberOfFoursCounter += 1

    return numberOfFoursCounter

def winningCondition(state: Board, turn: int):
    pieceList: list
    if turn == 0:
        pieceList = state.agentPlacedPieces

    elif turn == 1:
        pieceList = state.opponentPlacedPieces
                                      
    for piece in pieceList:
        #up
        counter = 0
        for i in range(piece.row, piece.row + 5):
            if i <= 14 and state.board[i][piece.col] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #down
        counter = 0
        for i in reversed(range(piece.row - 4, piece.row + 1)):
            if i >= 0 and state.board[i][piece.col] == turn:
                counter += 1
            else:break
            
            if counter == 5:
                return 1

        #left to right
        counter = 0
        for i in reversed(range(piece.col - 4, piece.col + 1)):
            if i >= 0 and state.board[piece.row][i] == turn:
                counter += 1
            else:
                break
            
            if counter == 5:
                return 1

        #right to left
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

def possibleMoves(state: Board, turn: int):
    moveSet = {}

    if state.turnNumber > 10:
        h = []
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.row+2):
                    if state.board[i][j] == -1:
                        loc = Location(i, j)
                        state.putPiece(loc, turn)
                        heapq.heappush(h, (-utility(state), Location(i, j)))
                        state.putPiece(loc, -1)

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.row+2):
                    if state.board[i][j] == -1:
                        loc = Location(i, j)
                        state.putPiece(loc, turn)
                        heapq.heappush(h, (-utility(state), Location(i, j)))
                        state.putPiece(loc, -1)

        for i in range(20):
            if not h:
                break
            else:
                moveSet[heapq.heappop(h)[1]] = 1
    elif state.turnNumber > 10:
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.row+2):
                    if state.board[i][j] == -1:
                        moveSet[Location(i, j)] = 1

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-1, piece.row+2):
                for j in range(piece.col-1, piece.row+2):
                    if state.board[i][j] == -1:
                        moveSet[Location(i, j)] = 1
    else:
        for piece in state.agentPlacedPieces:
            for i in range(piece.row-2, piece.row+3):
                for j in range(piece.col-2, piece.row+3):
                    if state.board[i][j] == -1:
                        moveSet[Location(i, j)] = 1

        for piece in state.opponentPlacedPieces:
            for i in range(piece.row-2, piece.row+3):
                for j in range(piece.col-2, piece.row+3):
                    if state.board[i][j] == -1:
                        moveSet[Location(i, j)] = 1


    return moveSet.keys()


def utility(state: Board):
    value = 0

    agentFours = numberOfFours(state, 0)
    agentStraightFours = numberOfStraightFours(state, 0)

    opponentFours = numberOfFours(state, 1)
    opponentStraightFours = numberOfStraightFours(state, 1)

    value += agentFours * 10
    value += agentStraightFours * 20
    value += numberOfThrees(state, 0)
    value += numberOfBrokenThrees(state, 0) * 4
    value += winningCondition(state, 0) * 1500

    value -= opponentFours * 15
    value -= opponentStraightFours * 30
    value -= numberOfThrees(state, 1) * 2
    value -= numberOfBrokenThrees(state, 1) * 6
    value -= winningCondition(state, 1) * 1000

    return value


def minValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 1) or depth == maximumDepth:
        return utility(state)

    value = sys.maxsize

    for location in possibleMoves(state, 0):
        state.putPiece(location, 0)
        value = min(value, maxValue(state, alpha, beta, depth + 1))
        state.putPiece(location, -1)
        if value <= alpha:
            return value
        beta = min(beta, value)

    return value


def maxValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 0) or depth == maximumDepth:
        return utility(state)

    value = -sys.maxsize

    for location in possibleMoves(state, 1):
        state.putPiece(location, 1)
        value = max(value, minValue(state, alpha, beta, depth + 1))
        state.putPiece(location, -1)
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value


def alphabetaSearch(state: Board):
    bestActionValue = -sys.maxsize
    bestAction = -1

    for location in possibleMoves(state, 0):

        state.putPiece(location, 0)

        if bestAction == -1:
            bestAction = location

        newValue = minValue(state, -sys.maxsize, sys.maxsize, 1)
        state.putPiece(location, -1)
        if newValue > bestActionValue:
            bestAction = location
            bestActionValue = newValue

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
            
        #agent.board.printBoard()
        
        
        if move == -1:
            print("no best move found")
            agent.io.write_move(possibleMoves(agent.board)[0])
        else:
            agent.io.write_move(move)
            agent.board.putPiece(move, 0)
        while agent.io.ready():
            pass
