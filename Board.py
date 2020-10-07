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
        
