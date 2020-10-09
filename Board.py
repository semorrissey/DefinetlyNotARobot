class Location:
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __hash__(self):
        return self.row * 57 + self.col * 71

    def __lt__(self, other):
        return self


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
        self.turnNumber = 1

    def putPiece(self, location: Location, piece: int):
        prev_val = self.board[location.row][location.col]
        self.board[location.row][location.col] = piece

        if piece == 0:
            self.agentPlacedPieces.append(location)
            self.turnNumber += 1

        elif piece == 1:
            self.opponentPlacedPieces.append(location)
            self.turnNumber += 1
            
        elif piece == -1 :
            # removes last placed piece
            if prev_val == 0:
                self.agentPlacedPieces.pop()
            elif prev_val == 1:
                self.opponentPlacedPieces.pop()

            self.turnNumber -= 1

    def printBoard(self):
        for i in range(15):
            for j in range(15):
                print(self.board[i][j], end=" ")
            print()
