from IO import *
from Board import *
from Agent import *

def buildBoard(agentLocations: list, opponentLocations: list):

    newBoard = Board()
    for location in agentLocations:
        newBoard.putPiece(location, 0)

    for location in opponentLocations:
        newBoard.putPiece(location, 1)

    return newBoard

#Testing Heuristics

def testStraightFours():
    agentLocations = []
    opponentLocations = []

    agentLocations.append(Location(0,0))
    agentLocations.append(Location(0,1))
    agentLocations.append(Location(0,2))
    agentLocations.append(Location(0,3))
    
    agentLocations.append(Location(1,1))
    agentLocations.append(Location(1,2))
    agentLocations.append(Location(1,3))
    agentLocations.append(Location(1,4))

    agentLocations.append(Location(13,13))
    agentLocations.append(Location(12,12))
    agentLocations.append(Location(11,11))
    agentLocations.append(Location(10,10))

    opponentLocations.append(Location(0,4))

    board = buildBoard(agentLocations, opponentLocations)
    testValue = numberOfStraightFours(board, 0)

    if testValue == 2:
        return True
    else:
        print("Number of straight fours seen: " + str(testValue))
        return False

def testFours():
    agentLocations = []
    opponentLocations = []

    agentLocations.append(Location(0,0))
    agentLocations.append(Location(0,1))
    agentLocations.append(Location(0,2))
    agentLocations.append(Location(0,3))
    
    agentLocations.append(Location(1,1))
    agentLocations.append(Location(1,2))
    agentLocations.append(Location(1,3))
    agentLocations.append(Location(1,4))

    agentLocations.append(Location(13,13))
    agentLocations.append(Location(12,12))
    agentLocations.append(Location(11,11))
    agentLocations.append(Location(10,10))

    opponentLocations.append(Location(9,9))

    board = buildBoard(agentLocations, opponentLocations)
    testValue = numberOfFours(board, 0)

    if testValue == 2:
        return True
    else:
        print("Number of fours seen: " + str(testValue))
        return False

def testThrees():
    agentLocations = []
    opponentLocations = []

    agentLocations.append(Location(0,0))
    agentLocations.append(Location(0,1))
    agentLocations.append(Location(0,2))

    agentLocations.append(Location(1,1))
    agentLocations.append(Location(1,2))
    agentLocations.append(Location(1,3))

    agentLocations.append(Location(1,5))
    agentLocations.append(Location(1,6))
    agentLocations.append(Location(1,7))

    agentLocations.append(Location(3,1))
    agentLocations.append(Location(4,1))
    agentLocations.append(Location(5,1))

    agentLocations.append(Location(12,2))
    agentLocations.append(Location(13,2))
    agentLocations.append(Location(14,2))

    opponentLocations.append(Location(0,8))
    opponentLocations.append(Location(1,8))
    opponentLocations.append(Location(2,8))
    opponentLocations.append(Location(3,8))

    board = buildBoard(agentLocations, opponentLocations)
    testValue = numberOfThrees(board, 0)

    if testValue == 2:
        return True
    else:
        print("Number of threes seen: " + str(testValue))
        return False
        
    
def testBrokenThrees():
    agentLocations = []
    opponentLocations = []

    agentLocations.append(Location(1,1))
    agentLocations.append(Location(2,2))
    agentLocations.append(Location(4,4))

    agentLocations.append(Location(0,12))
    agentLocations.append(Location(1,12))
    agentLocations.append(Location(3,12))

    agentLocations.append(Location(5,10))
    agentLocations.append(Location(5,11))
    agentLocations.append(Location(5,13))

    agentLocations.append(Location(12,0))
    agentLocations.append(Location(12,2))
    agentLocations.append(Location(12,3))

    agentLocations.append(Location(12,9))
    agentLocations.append(Location(12,10))
    agentLocations.append(Location(12,12))

    opponentLocations.append(Location(12,1))
    opponentLocations.append(Location(12,11))

    board = buildBoard(agentLocations, opponentLocations)
    testValue = numberOfBrokenThrees(board, 0)

    if testValue == 2:
        return True
    else:
        print("Number of broken threes seen: " + str(testValue))
        return False

def testWinningCondition():
    agentLocations = []
    opponentLocations = []

    agentLocations.append(Location(3,5))
    agentLocations.append(Location(4,5))
    agentLocations.append(Location(5,5))
    agentLocations.append(Location(6,5))

    opponentLocations.append(Location(5,6))
    opponentLocations.append(Location(7,5))
    opponentLocations.append(Location(7,6))
    opponentLocations.append(Location(7,7))
    opponentLocations.append(Location(7,8))

    non_winning_board = buildBoard(agentLocations, opponentLocations)

    agentLocations.append(Location(2,5))

    winning_board = buildBoard(agentLocations, opponentLocations)

    return winningCondition(winning_board, 0) and not winningCondition(non_winning_board, 0)

if not testStraightFours():
    print("Straight fours failed")

if not testFours():
    print("Fours failed")
    
if not testThrees():
    print("Threes failed")

if not testBrokenThrees():
    print("Broken Threes failed")

if not testWinningCondition():
    print("Winning condition failed")

print("All other tests passed")
