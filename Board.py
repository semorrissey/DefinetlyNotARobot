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

    def __init__(self):
        self.board = [[-1] * 15 for i in range(15)]
        self.agentPlacedPieces = []
        self.opponentPlacedPieces = []

    def putPiece(self, location: Location, piece: int):
        self.board[location.row][location.col] = piece

        if piece == 0:
            self.agentPlacedPieces.append(location)

        elif piece == 1:
            self.opponentPlacedPieces.append(location)

    def printBoard(self):
        for i in range(15):
            for j in range(15):
                print(self.board[i][j], end=" ")
            print()

    def bitchCopy(self):
        newBoard = Board()
        for location in self.agentPlacedPieces:
            newBoard.putPiece(location,0)
        for location in self.opponentPlacedPieces:
            newBoard.putPiece(location,1)
        return newBoard