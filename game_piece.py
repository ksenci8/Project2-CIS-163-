#Ksenija 2/26-2/27
#wrote class GamePiece
#Caleb 02/27
#fixed fuctionality of code working with starting code provided for the project
#Caleb 03/11
#created is_valid_placement method

#starter code imports
from position import Position
from player_colors import PlayerColors

#our code imports
from placeble import Placeble

class GamePiece(Placeble):
    def __str__(self):
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        last_row = len(board) - 1
        last_col = len(board[0]) - 1

        if not super().is_valid_placement(pos, board):
            return False

        if pos.col != 0:
            left = board[pos.row][pos.col - 1]
        else:
            return False
        if pos.col != last_col:
            right = board[pos.row][pos.col + 1]
        else:
            return False
        if pos.row != 0:
            up = board[pos.row - 1][pos.col]
        else:
            return False
        if pos.col != last_row:
            down = board[pos.row + 1][pos.col]
        else:
            return False



        if left is None:
            return True
        if right is None:
            return True
        if up is None:
            return True
        if down is None:
            return True


        if board[pos.row][pos.col] != left and right and up and down:
            return False
        return True

        # if board[pos.row][pos.col] != board[pos.row][pos.col-1] or board[pos.row][pos.col+1] or board[pos.row-1][pos.col] or board[pos.row+1][pos.col]:
        #     return False
        # return True




    #checking if two instances of GamePiece have the same color/value
    def __eq__(self, other):
        if self.color == other.color:
           return True
        return False




gamePiece1 = GamePiece(PlayerColors.BLACK)
gamePiece2 = GamePiece(PlayerColors.BLACK)
gamePiece3 = GamePiece(PlayerColors.WHITE)
print(gamePiece1 == gamePiece2) # prints True
print(gamePiece1 == gamePiece3) # prints False

