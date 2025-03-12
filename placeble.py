
#work by Ksenija (from 26th to 27th of February)
#wrote class Placeble

#Ksenija 02/26-02/27
#wrote class Placeble
#Caleb 02/27
#fixed functionality of code working with starting code provided for the project
#Ksenija 03/04
#Fixed small typo in is_valid_placement (was if pos.col < 0 or pos.row >= len(board[0])
#changed to if pos.col < 0 or pos.col >= len(board[0]))
#Caleb 03/11
#added docstrings to file

#starter code imports
from player_colors import PlayerColors
from position import Position

#our code imports
from abc import ABC, abstractmethod
from typing import List, Optional
from operator import truediv

class Placeble(ABC):
    '''
    creates color property and the abstractmethod for is_valid_placement

    Attributes:
        __color (PlayerColors): Object that is the color of the piece
    Methods:
        color(): property get method that returns __color
        __str__(): passes (no current str for class)
        is_valid_placement(pos, board): checks if pos is withing the confines of the board
        then checks if the position is empty if both are met returns True
    '''
    def __init__(self, color):
        '''
        Initializes the Placeable object and checks instance of color

        Args:
            __color(PlayerColors): Object that is the color of the piece
        Raises:
            TyperError: if color is not a PlayerColors object
        '''
        if not isinstance(color, PlayerColors):
            raise TypeError
        self.__color = color

    @property
    def color(self):
        '''
        Returns the __color value

        Returns:
             PlayerColors: The __color object
        '''
        return self.__color

    @abstractmethod
    def __str__(self):
        '''
        Abstract method that will be used by subclasses
        '''
        pass

    @abstractmethod
    def is_valid_placement(self, pos: Position, board):
        '''
        The Parent Method for checking validation of placement. Checks if pos is a position on
        the board then checks if the position is empty

        Returns:
            Bool: if conditions not met False if conditions met True
        '''

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
