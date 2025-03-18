#Ksenija 03/14
#Wrote the constructor for GoModel and the appropriate properties

from typing import List
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position

class UndoException(Exception):
    pass

class GoModel:
    #constructor
    def __init__(self, rows = 6, cols = 6):
        acceptable_values = [6, 9, 11, 13, 19]
        if rows != cols:
            raise ValueError
        if rows not in acceptable_values or cols not in acceptable_values:
            raise ValueError
        if not isinstance(rows, int):
            raise TypeError
        if not isinstance(cols, int):
            raise TypeError
        #Black starts the game first
        self.__current_player = GamePlayer(PlayerColors.BLACK)
        self.__nrows = rows
        self.__ncols = cols
        self.__board = []
        for x in range(rows):
            self.__board.append([])
            for _ in range(cols):
                self.__board[x].append(None)
        self.__message = 'Just message'
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
        #implemented the check from placeble
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise IndexError ('Out of bounds.')
        print(f"Getting piece at: ({pos.row}, {pos.col})")
        return self.__board[pos.row][pos.col]

    def set_piece(self, pos, piece = None):
        """
        Sets the piece's position on the board.
        """
        # if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
        #     raise IndexError ('Out of bounds.')
        if piece.is_valid_placement(pos, board):
            self.__board[pos.row][pos.col] = piece
        # print(f"Setting piece at ({pos.row}, {pos.col})")


    def set_next_player(self):
        """
        Changes the current player to the next, and thus, changes turn.
        """
        player1 = GamePlayer(PlayerColors.BLACK)
        player2 = Game Player2(PlayerColors.WHITE)
        self.__current_player = player1
        opponent_player = player2

    def pass_turn(self):
        """
        Skips the player's turn and updates the variable skip_count.
        """
        self.set_next_player()
        self._current_player.skip_count += 1

    def is_game_over(self):
        """
        Returns True if two consecutive skips are made.
        """
        if self._current_player.skip_count >= 2:
            return True
        return False

    def undo(self):
        pass

# g = GoModel()
#
# pos1 = Position(1, 1)
# piece1 = GamePiece(PlayerColors.BLACK)
#
# pos2 = Position(0, 0)
# piece2 = GamePiece(PlayerColors.WHITE)
#
# g.set_piece(pos1, piece1)
# g.set_piece(pos2, piece2)
#
# print(g.piece_at(pos1))
# print(g.piece_at(pos2))
# print('=========')
# print(g.piece_at(Position(2, 2)))  #print None (empty position)
# print(g.board)