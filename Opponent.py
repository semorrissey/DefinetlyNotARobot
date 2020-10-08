from IO import *
from Board import *
import copy
import sys


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
                numberOfBrokenThreesCounter += 1

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
                numberOfBrokenThreesCounter += 1

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
                numberOfBrokenThreesCounter += 1

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
        # diag right to left, up
        counter = 0
        for i in range(3):

            if not ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][
                piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][
                piece.col - 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            else:
                break

            if counter == 3:
                numberOfThreesCounter += 1

        # up
        counter = 0
        for i in range(3):

            if not ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                    piece.row - 3 >= 0 and state.board[piece.row - 3][piece.col] == -1)):
                break
            elif piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            else:
                break

            if counter == 3:
                numberOfThreesCounter += 1

        # diag left to right, up
        counter = 0
        for i in range(3):

            if not ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][
                piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][
                piece.col + 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            else:
                break

            if counter == 3:
                numberOfThreesCounter += 1

        # left to right
        counter = 0
        for i in range(piece.col, piece.col + 3):

            if not ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                    piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
                break
            elif i <= 14 and state.board[piece.row][i] == turn:
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
        # diag right to left, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][
                piece.col + 1] == -1) and (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][
                piece.col - 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfStraightFoursCounter += 1

        # up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) and (
                    piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
                break
            elif piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfStraightFoursCounter += 1

        # diag left to right, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][
                piece.col - 1] == -1) and (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][
                piece.col + 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfStraightFoursCounter += 1

        # left to right
        counter = 0
        for i in range(piece.col, piece.col + 4):

            if not ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) and (
                    piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
                break
            elif i <= 14 and state.board[piece.row][i] == turn:
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
        # diag right to left, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col + 1 <= 14 and state.board[piece.row + 1][
                piece.col + 1] == -1) ^ (piece.row - 4 >= 0 and piece.col - 4 >= 0 and state.board[piece.row - 4][
                piece.col - 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfFoursCounter += 1

        # up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and state.board[piece.row + 1][piece.col] == -1) ^ (
                    piece.row - 4 >= 0 and state.board[piece.row - 4][piece.col] == -1)):
                break
            elif piece.row - i >= 0 and state.board[piece.row - i][piece.col] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfFoursCounter += 1

        # diag left to right, up
        counter = 0
        for i in range(4):

            if not ((piece.row + 1 <= 14 and piece.col - 1 >= 0 and state.board[piece.row + 1][piece.col - 1] == -1) ^ (piece.row - 4 >= 0 and piece.col + 4 <= 14 and state.board[piece.row - 4][piece.col + 4] == -1)):
                break
            elif piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            else:
                break

            if counter == 4:
                numberOfFoursCounter += 1

        # left to right
        counter = 0
        for i in range(piece.col, piece.col + 4):

            if not ((piece.col - 1 >= 0 and state.board[piece.row][piece.col - 1] == -1) ^ (piece.col + 4 <= 14 and state.board[piece.row][piece.col + 4] == -1)):
                break
            elif i <= 14 and state.board[piece.row][i] == turn:
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
        # up
        counter = 0
        for i in range(piece.row, piece.row + 5):
            if i <= 14 and state.board[i][piece.col] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True

        # down
        counter = 0
        for i in reversed(range(piece.row - 4, piece.row + 1)):
            if i >= 0 and state.board[i][piece.col] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True

        # left to right
        counter = 0
        for i in reversed(range(piece.col - 4, piece.col + 1)):
            if i >= 0 and state.board[piece.row][i] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True

        # right to left
        counter = 0
        for i in range(piece.col, piece.col + 5):
            if i <= 14 and state.board[piece.row][i] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True

        # diag right to left, up
        counter = 0
        for i in range(5):
            if piece.row - i >= 0 and piece.col - i >= 0 and state.board[piece.row - i][piece.col - i] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True

        # diag left to right up
        counter = 0
        for i in range(5):
            if piece.row - i >= 0 and piece.col + i <= 14 and state.board[piece.row - i][piece.col + i] == turn:
                counter += 1
            else:
                break

            if counter == 5:
                return True


def possibleMoves(state: Board):
    moveSet = []
    for i in range(15):
        for j in range(15):
            if state.board[i][j] == -1:
                moveSet.append(Location(i, j))

    return moveSet


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

    value -= opponentFours * 10
    value -= opponentStraightFours * 20
    value -= numberOfThrees(state, 1)
    value -= numberOfBrokenThrees(state, 1) * 4

    return value


def minValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 1) or depth == maximumDepth:
        return utility(state)

    value = sys.maxsize

    for location in possibleMoves(state):
        newState = state.bitchCopy()
        newState.putPiece(location, 0)
        value = min(value, maxValue(newState, alpha, beta, depth + 1))
        if alpha <= beta:
            return value
        beta = min(beta, value)

    return value


def maxValue(state: Board, alpha: int, beta: int, depth: int):
    if winningCondition(state, 0) or depth == maximumDepth:
        return utility(state)

    value = -sys.maxsize

    for location in possibleMoves(state):
        newState = state.bitchCopy()
        newState.putPiece(location, 1)
        value = max(value, minValue(newState, alpha, beta, depth + 1))
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value


def alphabetaSearch(state: Board):
    bestActionValue = -sys.maxsize
    bestAction = -1

    for location in possibleMoves(state):

        newState = state.bitchCopy()
        newState.putPiece(location, 0)

        if (bestAction == -1):
            bestAction = location

        newValue = maxValue(newState, -sys.maxsize, sys.maxsize, 1)
        if (newValue > bestActionValue):
            bestAction = location
            bestActionValue = newValue

    return bestAction


agent = Agent()

while (not game_over()):
    while (agent.io.ready()):
        rd = read_move()
        if not rd == -1:
            print("row: " + str(rd.row) + ", col: " + str(rd.col))
            agent.board.putPiece(rd, 1)
        agent.board.printBoard()
        move = alphabetaSearch(agent.board)
        if move == -1:
            print("no best move found")
            agent.io.write_move(possibleMoves(agent.board)[0])
        else:
            agent.io.write_move(move)
            agent.board.putPiece(move, 0)
        while agent.io.ready():
            pass

