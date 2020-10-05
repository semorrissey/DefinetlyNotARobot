class Board:
    # -1 empty, 0 white piece, 1 black piece
    board: list
    placedPieces: list

    def __init__(self):
        self.board = [[-1] * 15 for i in range(15)]

    def setPiece(self, x: int, y: int, piece: int):
        self.board[x][y] = int


class Location:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
