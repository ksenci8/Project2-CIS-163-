#Ksenija 2/26-2/27
#wrote class GamePiece
#Caleb 02/27
#fixed functionality of code working with starting code provided for the project
##Ksenija 03/01
#Developed the majority of the logic in is_valid_placement
#Ksenija 03/07
#Polished the is_valid_placement
#Caleb 03/11
#created is_valid_placement method
#Ksenija 03/12
#Further work on is_valid_placement and testing


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
        #Last row and column index
        last_row = len(board) - 1
        last_col = len(board[0]) - 1

        left = board[pos.row][pos.col - 1]
        right = board[pos.row][pos.col + 1]
        up = board[pos.row - 1][pos.col]
        down = board[pos.row + 1][pos.col]
        occupied_count = 0
        player_piece = PlayerColors.BLACK
        opponent_piece = player_piece.opponent()

        # Checking for edge case scenarios (corners)
        if pos.row == 0 or pos.row == last_row:  # First or last row
            if up == opponent_piece:
                occupied_count += 1
            if pos.row < last_row and right == opponent_piece:
                occupied_count += 1
            if down == opponent_piece:
                occupied_count += 1
            if left == opponent_piece:
                occupied_count += 1

        # First or last column
        if pos.col == 0 or pos.col == last_col:
            if up == opponent_piece:
                occupied_count += 1
            if right == opponent_piece:
                occupied_count += 1
            if down == opponent_piece:
                occupied_count += 1
            if left == opponent_piece:
                occupied_count += 1

        if occupied_count == 3:
            return False

        # The general scenario, checking for four places
        occupied_count = 0
        # checking left
        if left == opponent_piece:
            occupied_count += 1
        # checking right
        if right == opponent_piece:
            occupied_count += 1
        # checking up
        if up == opponent_piece:
            occupied_count += 1
        # checking down
        if down == opponent_piece:
            occupied_count += 1
        # will be checked last
        if occupied_count == 4:
            return False
        return True

    #checking if two instances of GamePiece have the same color/value
    def __eq__(self, other):
        if self.color == other.color:
           return True
        return False

pos = Position(2,2)
board = [
    [None, None, None, None, None],
    [None, PlayerColors.WHITE, PlayerColors.WHITE, None, None],
    [None, PlayerColors.WHITE, None, PlayerColors.WHITE, None],  # Checking (2,2) for Black
    [None, None, PlayerColors.WHITE, None, None],
    [None, None, None, None, None]
]

g = GamePiece(PlayerColors.BLACK)
print(g.is_valid_placement(pos, board))
# gamePiece1 = GamePiece(PlayerColors.BLACK)
# gamePiece2 = GamePiece(PlayerColors.BLACK)
# gamePiece3 = GamePiece(PlayerColors.WHITE)
# print(gamePiece1 == gamePiece2) # prints True
# print(gamePiece1 == gamePiece3) # prints False
#
