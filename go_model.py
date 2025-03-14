#Ksenija 03/14
#Wrote the constructor for GoModel and the appropriate properties
from typing import List
from game_player import GamePlayer

class UndoException(Exception):
    pass
class GoModel:
    #constructor

    def __init__(self, rows: int = 6, cols: int = 6):
        acceptable_values = [6, 9, 11, 13, 19]
        if not isinstance(current_player, GamePlayer):
            raise TypeError
        if not isinstance(rows, int):
            raise TypeError
        # raising ValueError for nrows and ncols
        if rows not in acceptable_values or cols not in acceptable_values:
            raise ValueError
        if not isinstance(cols, int):
            raise TypeError
        # if not isinstance(board, ):
        #     raise TypeError
        if not isinstance(message, str):
            raise TypeError
        if not isinstance(rows, int):
            raise TypeError
        if not isinstance(cols, int):
            raise TypeError
        self.__current_player = PlayerColor.BLACK
        self.__nrows = rows
        self.__ncols = cols
        self.__board = []
        for x in range(rows):
            self.__board.append([])
            for _ in range(cols):
                self.__board[x].append(None)
        self.__message = message
    # properties
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
    @property 
    def message(self):
        return self.__message
    @message.setter
    def message(self, mes):
        if not isinstance(mes, str):
            raise TypeError
        self.__message = mes

    def set_piece(self):
        pass