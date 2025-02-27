#maybe just import the files into this one.

from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Optional

# from player_colors import PlayerColors
# from position import Position
# from go_gui_view import GUI

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
    def is_valid_placement(self, pos: Position, board: List[List[Optional[GamePiece]]]):
        pass

