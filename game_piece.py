#Ksenija from 02/26 to 02/27
#wrote class GamePiece
#Caleb 02/27
#fixed fuctionality of code working with starting code provided for the project
#Ksenija 03/01
#Wrote out the majority of the logic for checking if player is occupied by opponent
#in is_valid_placement

#starter code imports
from position import Position
from player_colors import PlayerColors
#our code imports
from placeble import Placeble

class GamePiece(Placeble):
    def __str__(self):
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        left = board[pos.row][pos.col-1]
        right = board[pos.row][pos.col+1]
        up = board[pos.row-1][pos.col]
        down = board[pos.row+1][pos.col]
        occupied_count = 0
        player_piece = PlayerColors.BLACK
        opponent_piece = player_piece.opponent()
        #checking left
        if left == opponent_piece:
            occupied_count +=1
        #checking right
        if right == opponent_piece:
            occupied_count +=1
        #checking up
        if up == opponent_piece:
            occupied_count +=1
        #checking down
        if down == opponent_piece:
            occupied_count +=1
        #Checking for corner scenarios, three places need to be occupied
        last_row = len(board) - 1
        last_col = len(board[0]) - 1
        #First row
        if pos.row == 0:
            if pos.row > 0 and up == opponent_piece:
                occupied_count +=1
            if pos.col < last_col and right == opponent_piece:
                occupied_count += 1
            if down == opponent_piece:
                occupied_count += 1
        #Last row

        #will be checked last
        if occupied_count == 4:
            return True







        ''' I believe this will just use the parent function and then add on the checking for when
        the user is trying to place a piece in a spot that is surrounded by the opponent's pieces'''



    #checking if two instances of GamePiece have the same color/value
    def equals(self, other):
       if not isinstance(other, GamePiece):
           return False
       return True

# gamePiece1 = GamePiece(PlayerColors.BLACK)
# gamePiece2 = GamePiece(PlayerColors.BLACK)
# gamePiece3 = GamePiece(PlayerColors.WHITE)
# print(gamePiece1 == gamePiece2) # prints True
# print(gamePiece1 == gamePiece3) # prints False