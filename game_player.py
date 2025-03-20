#Caleb 03/13
#Wrote all methods
#Caleb
#Wrote docstrings
from player_colors import PlayerColors

class GamePlayer:
    '''
    Class to keep track of a Player including there Color, capture count, and skip count

    Attributes:
        __player_color(PlayerColors): Color of the Player's pieces
        __capture_count(int): ammount the Player has captured
        __skip_count(int): ammount of times the Player has skipped
    Methods:
        player_color(): property get method for __player_color
        capture_count(): property get method for __capture_count
        capture_count(num): property setter method for __capture_count
        skip_count(): property get method for __skip_count
        skip_count(num): property setter method for __skip_count
        __str__(): print output for printing an object
    '''
    def __init__(self, player_color: PlayerColors, capture_count=0, skip_count=0):
        '''
        Initializes GamePlayer object and makes TypeError checks for the parameters

        Args:
            __player_color(PlayerColors): Color of the Player's pieces
            __capture_count(int): ammount the Player has captured
            __skip_count(int): ammount of times the Player has skipped
        Raises:
            TypeError: if player_color is not an object of PlayerColors
            TypeError: if capture_count is not an int
            TypeError: if skip_count is not an int
        '''
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
        '''
        Property get method for __player_color

        Returns:
            PlayerColors: the player's color
        '''
        return self.__player_color

    #capture_count getter/setter
    @property
    def capture_count(self):
        '''
        Property get method for __capture_count

        Returns:
             Int: the player's capture count
        '''
        return self.__capture_count
    @capture_count.setter
    def capture_count(self, num):
        '''
        property setter for __capture_count

        Raises:
            TypeError: if num is not an int
            ValueError: if num is below 0
        '''
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__capture_count = num

    #skip_count getter/setter
    @property
    def skip_count(self):
        '''
        Property get method for __skip_count

        Returns:
             Int: the player's skip count
        '''
        return self.__skip_count
    @skip_count.setter
    def skip_count(self, num):
        '''
        property setter for __skip_count

        Raises:
            TypeError: if num is not an int
            ValueError: if num is below 0
        '''
        if not isinstance(num, int):
            raise TypeError
        if num < 0:
            raise ValueError
        self.__skip_count = num

    def __str__(self):
        '''
        Printing output for printing an Object

        Returns:
             str: string for debugging GamePlayer objects
        '''
        return f'player_color: {self.__player_color}\ncapture_count: {self.__capture_count}\n skip_count: {self.__skip_count}'
    #the __str__ method was up to us for debugging I decided this was a good format ^^^