#work by Ksenija (from 26th to 27th of February)
#wrote class GamePiece

from placeble import Placeble
from enum import Enum
class Position:
    def __init__(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError
        self.row = row
        self.col = col
class GamePiece(Placeble):
    def __str__(self):
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        if not isinstance(pos, Position):
            raise TypeError
        #checking if the position is within the board
        if pos.row < 0 or pos.row >= len(board):
            return False
        if pos.col < 0 or pos.row > len(board[0]):
            return False
        #checking if the place on board is empty
        if board[pos.row] and board[pos.col] is None:
            return False
        return True
    #checking if two instances of GamePiece have the same color/value
    def equals(self, other ):
       if not isinstance(other, GamePiece):
           return False
       return True

# gamePiece1 = GamePiece(PlayerColors.BLACK)
# gamePiece2 = GamePiece(PlayerColors.BLACK)
# gamePiece3 = GamePiece(PlayerColors.WHITE)
# print(gamePiece1 == gamePiece2) # prints True
# print(gamePiece1 == gamePiece3) # prints False
