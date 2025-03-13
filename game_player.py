#Caleb 03/13
#Wrote all methods

from player_colors import PlayerColors

class GamePlayer:

    def __init__(self, player_color: PlayerColors, capture_count=0, skip_count=0):
        if not isinstance(player_color, PlayerColors):
            raise TypeError
        if not isinstance(capture_count, int):
            raise TypeError
        if not isinstance(skip_count, int):
            raise TypeError
        self.__player_color = player_color
        self.__capture_count = capture_count
        self.__skip_count = skip_count

    #player_color getter
    @property
    def player_color(self):
        return self.__player_color

    #capture_count getter/setter
    @property
    def capture_count(self):
        return self.__capture_count
    @capture_count.setter
    def capture_count(self, num):
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__capture_count = num

    #skip_count getter/setter
    @property
    def skip_count(self):
        return self.__skip_count
    @skip_count.setter
    def skip_count(self, num):
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__skip_count = num

    def __str__(self):
        return f'player_color: {self.__player_color}\ncapture_count: {self.__capture_count}\n skip_count: {self.__skip_count}'
    #the __str__ method was up to us for debugging I decided this was a good format ^^^