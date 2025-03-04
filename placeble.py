
#work by Ksenija (from 26th to 27th of February)
#wrote class Placeble

#work by Ksenija (from 26th to 27th of February)
#wrote class Placeble
#Should we do a more concise method now that we both understand what we are doing up here like this:
#Caleb 02/27
#fixed functionality of code working with starting code provided for the project
#Ksenija 03/04
#Fixed small typo in is_valid_placement (was if pos.col < 0 or pos.row >= len(board[0])
#changed to if pos.col < 0 or pos.col >= len(board[0]))


#starter code imports
from player_colors import PlayerColors
from position import Position

#our code imports
from abc import ABC, abstractmethod
from typing import List, Optional
from operator import truediv

class Placeble(ABC):
    def __init__(self, color):
        if not isinstance(color, PlayerColors):
            raise TypeError
        self.__color = color

    @property
    def color(self):
        return self.__color
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def is_valid_placement(self, pos: Position, board):
        if not isinstance(pos, Position):
            return False

        #checking if the position is within the board
        if pos.row < 0 or pos.row >= len(board):
            return False
        if pos.col < 0 or pos.col >= len(board[0]):
            return False
        #checking if the place on board is empty
        if board[pos.row][pos.col] is not None:
            return False
        return True
