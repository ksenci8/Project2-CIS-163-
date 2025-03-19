#Ksenija 03/14
#Wrote the constructor for GoModel and the appropriate properties
#Caleb 03/18
#worked on is_valid_placement checkin if placement reverts to the previous board position and undo method
import copy
from typing import List
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position
import copy

class UndoException(Exception):
    pass

class GoModel:
    #constructor
    def __init__(self, rows = 6, cols = 6):
        acceptable_values = [6, 9, 11, 13, 19]
        if not isinstance(rows, int):
            raise TypeError
        if not isinstance(cols, int):
            raise TypeError
        if rows != cols:
            raise ValueError
        if rows not in acceptable_values or cols not in acceptable_values:
            raise ValueError
        #Black starts the game first
        self.__current_player = GamePlayer(PlayerColors.BLACK)
        self.__nrows = rows
        self.__ncols = cols
        self.__board = []
        self.player1 = GamePlayer(PlayerColors.BLACK)
        self.player2 = GamePlayer(PlayerColors.WHITE)
        for x in range(rows):
            self.__board.append([])
            for _ in range(cols):
                self.__board[x].append(None)
        self.__message = 'This is default value for message'

        #attributes I am experimenting with for undo()
        self.moves = {
            0 : self.board
        }
        self.move_num = 0
        self.previous_board = []

    # Properties
    @property
    def nrows(self):
        return self.__nrows
    @property
    def ncols(self):
        return self.__ncols
    @property
    def current_player(self):
        return self.__current_player
    @property
    def board(self):
        return self.__board
    #I know board.setter is not specified in the project, but I created for usage in undo()
    # @board.setter
    # def board(self, board):
    #     self.__board = board
    #message getter and setter
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, mes):
        if not isinstance(mes, str):
            raise TypeError
        self.__message = mes

    def piece_at(self, pos):
        """
        Returns the piece's position on the board and checks if the position
        is out of bounds.
        """
        # implemented the check from placeble
        if not isinstance(pos, Position):
            raise TypeError
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise IndexError ('Out of bounds.')
        print(f"Getting piece at: ({pos.row}, {pos.col})")
        return self.__board[pos.row][pos.col]

    def set_piece(self, pos, piece = None):
        """
        Sets the piece's position on the board.
        """
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise IndexError ('Out of bounds.')
        if piece.is_valid_placement(pos, self.__board):
            self.moves[self.move_num] = self.copy_board() #creates the previous board onto the moves dict
            self.__board[pos.row][pos.col] = piece
            self.move_num += 1 #updates the number of moves done
        # print(f"Setting piece at ({pos.row}, {pos.col})")


    def set_next_player(self):
        """
        Changes the current player to the next, and thus, changes turn.
        """
        #two attributes
        #if one, do the other
        if self.__current_player == self.player1:
            self.__current_player = self.player2
        #same
        elif self.__current_player == self.player2:
            self.__current_player = self.player1
        # else:
        #     self.__current_player = GamePlayer(PlayerColors.BLACK)
        # player1 = GamePlayer(PlayerColors.BLACK)
        # player2 = GamePlayer(PlayerColors.WHITE)
        # self.__current_player = player1
        # opponent_player = player2


    def pass_turn(self):
        """
        Skips the player's turn and updates the player's skip_count.
        """
        self.set_next_player()
        self.__current_player.skip_count += 1

    def is_game_over(self):
        """
        Returns True if two consecutive skips are made.
        """
        if self.__current_player.skip_count >= 2:
            return True
        return False

    #DOESN'T WORK yet
    def is_valid_placement(self, pos, piece):
        if not piece.is_valid_placement(pos, self.board):
            self.message = ('Invalid Placement: Either not within bounds,\n'
                            'or piece is already surrounded by opponent pieces')
            return False
        #temp_board = self.board
        temp_board = self.copy_board()
        print(f'This is temp board: {temp_board}')
        print('=======')
        print(f'This is board:{self.board}')
        temp_board[pos.row][pos.col] = piece
        if temp_board == self.previous_board:
            return False
        return True


    def undo(self): #NEEDS FIXING for when undo() is ran right away and UndoException() should raise but doesn't
        if not self.moves: #raises UndoException when
            raise UndoException('Nothing to Undo')
        self.board = self.moves[self.move_num-1] #takes the previous move_num (the keys for moves) which gives the board 1 move earlier
        self.set_next_player() #switches the player turn to the other.
        self.previous_board = self.moves.pop(self.move_num-1) #keeping previous hand is purely for the is_valid_placement check.
        # but since its a pop its also for removing it
        self.move_num -= 1 #brings the current move_num down 1

    def copy_board(self):
        return copy.deepcopy(self.board)


    # def copy_board(self):
    #     b = []
    #     # loop = -1
    #     for row in self.board:
    #         updated_row = []
    #         # b.append([])
    #         # loop += 1
    #         #for x in i:
    #         for square in row:
    #             updated_row.append(square)
    #         b.append(updated_row)
    #     return b


#Message works and the checks work
# go = GoModel()
# pos = Position(1, 1)
# piece = GamePiece(PlayerColors.BLACK)
#
#
# valid = go.is_valid_placement(pos, piece)
# print(valid)  # Either True or False based on pos
# print(go.message)  # Prints message
go = GoModel()  # Assuming Game is the class with the methods
go.pass_turn()  # Player 1 skips
print(go.current_player)  # Should print WHITE (next player)

go.pass_turn()  # Player 2 skips
print(go.current_player)  # Should print BLACK (next player)

# Check if game is over
if go.is_game_over():
    print("Game Over!")  # Should print over after two skips
else:
    print("Game continues.")


# g = GoModel()
# print(g.current_player)
# print(f'\ndefault moves:{g.moves} \n')
# pos1 = Position(1, 1)
# piece1 = GamePiece(PlayerColors.BLACK)
#
# pos2 = Position(0, 0)
# piece2 = GamePiece(PlayerColors.WHITE)
#
# g.set_piece(pos1, piece1)
# g.set_piece(pos2, piece2)
# print(g.board)
# g.undo()
# print(g.board)
# g.set_piece(pos2, piece2)
# print(g.board)

# print(g.board)
# print('moves:\n')
# for i in g.moves.keys():
#     print(f'move: {i} board: {g.moves[i]}')
# print('\n')
#
# g.undo()
# print(g.board)
# g.undo()
# print(g.board)
# g.undo()


#
# print(g.piece_at(pos1))
# print(g.piece_at(pos2))
# print('=========')
# print(g.piece_at(Position(2, 2)))  #print None (empty position)
# print(g.board)