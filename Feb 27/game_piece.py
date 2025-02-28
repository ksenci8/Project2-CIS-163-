#work by Ksenija (from 26th to 27th of February)
#wrote class GamePiece
#Caleb 02/27
#fixed fuctionality of code working with starting code provided for the project

#starter code imports
from position import Position

#our code imports
from placeble import Placeble

class GamePiece(Placeble):
    def __str__(self):
        return f'Color: {self.color}'

    def is_valid_placement(self, pos: Position, board):
        ''' I believe this will just use the parent function and then add on the checking for when
        the user is trying to place a piece in a spot that is surrounded by the oppenent's pieces'''



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
