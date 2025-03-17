#Ksenija 2/26-2/27
#wrote class GamePiece
#Caleb 02/27
#fixed functionality of code working with starting code provided for the project
#Ksenija 03/01
#Developed the majority of the logic in is_valid_placement
#Ksenija 03/07
#Polished the is_valid_placement
#Caleb 03/11
#created is_valid_placement method
#Ksenija 03/12
#Further work on is_valid_placement and testing
#Caleb 03/11
#attempted at creating is_valid_placement method fixed equals method to __eq__
#Caleb 03/11
#polished is_valid_placement but still contains error when uploaded
#Ksenija 03/16
#Added docstrings


#starter code imports
from position import Position
from player_colors import PlayerColors

#our code imports
from placeble import Placeble

class GamePiece(Placeble):
    """
    Represents the game piece, checks valid placement on board, and inherits Placeble class.
    Methods: 
        is_valid_placement(pos, board): Checks that placement is valid if not occupied by opponent pieces.
        __eq__(): Compares two game pieces and returns True if they have the same value.
    """
    def __str__(self):
        """
        Returns the color of game piece and serves for debugging purposes.
        :return:
        """
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        """
        Expands on Placeble's is_valid_placement and returns the appropriate
        boolean value based on validity of placement of player piece (True if yes, False if not).
        First, it checks if the position is valid based on the parent class.
        Second, it ensures that the position is not out of bounds (outside the board),
        and stores the created adjacent squares (left, right, up, and down) into a list adjacent.
        Lastly, it counts the adjacent squares occupied by the opponent pieces. If all
        are occupied, it returns False (placement invalid), else True (placement is valid).
        """
        if not super().is_valid_placement(pos, board):
            return False

        last_row = len(board) - 1
        last_col = len(board[0]) - 1
        # checks if the direction would cause an error if it wouldn't then it creates the direction
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

        # iterates through adjacent tallying when there is an opponent piece
        for i in adjacent:
            if i is None:
                pass
            elif i == opponent_piece:
                occupied_count += 1
        if occupied_count == len(adjacent):
            return False
        return True


    #checking if two instances of GamePiece have the same color/value
    def __eq__(self, other):
        """
        Compares two instances of GamePiece and returns True if their value
        is same, or returns False if the value is different.
        """
        if self.color == other:
           return True
        return False


# pos = Position(2,4)
    # board = [
    #     [None, None, None, None, None],
    #     [None, PlayerColors.WHITE, PlayerColors.WHITE, None, None],
    #     [None, PlayerColors.WHITE, None, PlayerColors.WHITE, None],  # Checking (2,2) for Black
    #     [None, None, PlayerColors.WHITE, None, None],
    #     [None, None, None, None, None]
# ]
#
# g = GamePiece(PlayerColors.BLACK)
# print(g.is_valid_placement(pos, board))
# gamePiece1 = GamePiece(PlayerColors.BLACK)
# gamePiece2 = GamePiece(PlayerColors.BLACK)
# gamePiece3 = GamePiece(PlayerColors.WHITE)
# print(gamePiece1 == gamePiece2) # prints True
# print(gamePiece1 == gamePiece3) # prints False
#
