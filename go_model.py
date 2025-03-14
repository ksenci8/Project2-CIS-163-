#Ksenija 03/14
#Wrote the constructor for GoModel and the appropriate properties
from typing import List
from game_player import GamePlayer

class UndoException(Exception):
    pass
class GoModel:
    #constructor

    def __init__(self, rows: int, cols: int):
        acceptable_values = [6, 9, 11, 13, 19]
        if not isinstance(current_player, GamePlayer):
            raise TypeError
        if not isinstance(nrows, int):
            raise TypeError
        # raising ValueError for nrows and ncols
        if nrows not in acceptable_values or ncols not in acceptable_values:
            raise ValueError
        if not isinstance(ncols, int):
            raise TypeError
        if not isinstance(board,List[List[GamePiece|None]]):
            raise TypeError
        if not isinstance(message, str):
            raise TypeError
        if not isinstance(rows, int):
            raise TypeError
        if not isinstance(cols, int):
            raise TypeError
        self.__current_player = current_player
        self.__nrows = nrows
        self.__ncols = ncols
        self.__board = board
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
    pass