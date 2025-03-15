#Ksenija 2/26-2/27
#wrote class GamePiece
#Caleb 02/27
#fixed fuctionality of code working with starting code provided for the project
#Caleb 03/11
#attempted at creating is_valid_placement method fixed equals method to __eq__
#Caleb 03/11
#polished is_valid_placement but still contains error when uploaded

#starter code imports
from position import Position
from player_colors import PlayerColors

#our code imports
from placeble import Placeble

class GamePiece(Placeble):
    def __str__(self):
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        if not super().is_valid_placement(pos, board):
            return False

        last_row = len(board) - 1
        last_col = len(board[0]) - 1
        #checks if the direction would cause an error if it wouldn't then it creates the direction
        # and appends it to adjacent which is a list to keep track of them
        adjacent = []
        if pos.col != 0:
            left = board[pos.row][pos.col - 1]
            adjacent.append(left)
        if pos.col != last_col:
            right = board[pos.row][pos.col + 1]
            adjacent.append(right)
        if pos.row != 0:
            up = board[pos.row - 1][pos.col]
            adjacent.append(up)
        if pos.row != last_row:
            down = board[pos.row + 1][pos.col]
            adjacent.append(down)

        player_piece = self.color
        opponent_piece = player_piece.opponent()
        occupied_count = 0

        #iterates through adjacent tallying when there is an opponent piece
        for i in adjacent:
            if i == opponent_piece:
                occupied_count += 1
        if occupied_count == len(adjacent):
            return False
        return True


    #checking if two instances of GamePiece have the same color/value
    def __eq__(self, other):
        if self.color == other.color:
           return True
        return False




pos = Position(4,4)
board = [
    [None, PlayerColors.BLACK, None, PlayerColors.BLACK, None],
    [PlayerColors.BLACK, None, PlayerColors.BLACK, None, PlayerColors.BLACK],
    [None, PlayerColors.BLACK, None, PlayerColors.BLACK, None],
    [PlayerColors.BLACK, None, PlayerColors.BLACK, None, PlayerColors.BLACK],
    [None, PlayerColors.BLACK, None, PlayerColors.BLACK, None]
]

g = GamePiece(PlayerColors.WHITE)
print(g.is_valid_placement(pos, board))

# gamePiece1 = GamePiece(PlayerColors.BLACK)
# gamePiece2 = GamePiece(PlayerColors.BLACK)
# gamePiece3 = GamePiece(PlayerColors.WHITE)
# print(gamePiece1 == gamePiece2) # prints True
# print(gamePiece1 == gamePiece3) # prints False

