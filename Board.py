class Location:
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class Board:
    # -1 empty, 0 agent, 1 opponent
    board: list
    agentPlacedPieces: list
    opponentPlacedPieces: list
    turnNumber: int

    def __init__(self):
        self.board = [[-1] * 15 for i in range(15)]
        self.agentPlacedPieces = []
        self.opponentPlacedPieces = []
        self.turnNumber = 0

    def putPiece(self, location: Location, piece = -1):
        prev_val = self.board[location.row][location.col]
        self.board[location.row][location.col] = piece

        if piece == 0:
            self.agentPlacedPieces.append(location)
            turnNumber += 1

        elif piece == 1:
            self.opponentPlacedPieces.append(location)
            turnNumber += 1
            
        elif piece == -1 :
            # removes last placed piece
            if prev_val == 0:
                self.agentPlacedPieces.pop()
            elif prev_val == 1:
                self.opponentPlacedPieces.pop()

            turnNumber -= 1

    def printBoard(self):
        for i in range(15):
            for j in range(15):
                print(self.board[i][j], end=" ")
            print()
