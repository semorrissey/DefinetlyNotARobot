class Location:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Board:
    # -1 empty, 0 agent, 1 opponent
    board: list
    agentPlacedPieces: list
    opponentPlacedPieces: list

    def __init__(self):
        self.board = [[-1] * 15 for i in range(15)]

    def putPiece(self, location: Location, piece: int):
        self.board[location.x][location.y] = piece

        if piece == 0:
            agentPlacedPieces.append(location)

        else if piece == 1:
            opponentPlacedPieces.append(location)
        
