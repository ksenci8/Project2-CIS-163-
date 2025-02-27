
#work by Ksenija (from 26th to 27th of February)
#wrote class Placeble

from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Optional

class PlayerColors(Enum):
    BLACK = 0
    WHITE = 1

    def opponent(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]
class Position:
    def __init__(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError
        self.row = row
        self.col = col

    def __str__(self):
        output = f'Placed Go Game piece at [{self.row}, {self.col}]'
        return output

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
        pass

