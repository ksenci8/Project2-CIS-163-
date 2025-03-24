#Ksenija 03/14
#Wrote the constructor for GoModel and the appropriate properties
#Ksenija 03/17
#Wrote out methods set_piece, piece_at, game_over, pass_turn
#Ksenija 03/18
#Further work on GoModel
#Caleb 03/18
#worked on is_valid_placement checking if placement reverts to the previous board position and undo method
#Ksenija 03/19
#Fixed piece_at and pass_turn
#Caleb 03/19
#worked on undo() and is_valid_placement. while working on those had to change somethings in the constructor and set_piece
import copy
from typing import List
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position
import copy

class UndoException(Exception):
    """
    Called when there are no moves left to undo.

    Raises:
    	Undo: If no moves left to undo.
    """
    pass

class GoModel:
    """
    Represents the model to play the game Go. Implements appropriate methods to check
    valid placement of piece, playing turns between players, undo a previous move, calculates the score, and
    ensures game is over if conditions are met (two consecutive passes made by both players).

    Attributes:
        rows(int) = Represents the board's rows and the default value is 6.
        cols(int) = Represents the board's rows and the default value is 6.
    Instance variables:
        __current_player = Represents the current player (Black starts first).
         __nrows = Represents the number of rows and takes rows as value.
        __ncols = Represents the number of columns and takes cols as value.
        __board = Represents the board of the game.
        __player1 = Represents the black player and used primarily in set_next_player.
        __player2 = Represents the white player and used primarily in set_next_player.
        consecutive_pass = Tracks the number of consecutive passes and used for is_game_over.
        __message = Displays the message throughout the game.
        previous_board = Represents the previous board state.
    Methods:
        piece_at(pos): Checks the position of the piece.
        set_piece(pos, piece): Sets the piece at a given position.
        set_next_player(): Changes from player1 to player2 or vice versa.
        pass_turn(): Uses set_next_player and passes a turn.
        is_game_over: Checks if the variable consecutive_pass is equal to 2 and returns True.
        is_valid_placement(pos, piece): Expands the previous version of this method by checking if placement
        would result in previous board state.
        undo(): Undos the most recent move that has not yet been undone.
        copy_board(): creates a copy of the board with the same GamePiece refernces
    """
    def __init__(self, rows = 6, cols = 6):
        """
        Initializes the GoModel object.

        Args:
            rows = Number of rows and default value is 6.
            cols = Number of columns and default value is 6.
        Raises:
            TypeError: if rows is not an integer; if columns in not an integer.
            ValueError: If the value of rows and columns is anything else other than acceptable values.
            ValueError: If rows and cols aren't the same ammount (if board is a rectangle)
        """
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
        self.__player1 = GamePlayer(PlayerColors.BLACK)
        self.__player2 = GamePlayer(PlayerColors.WHITE)
        #added this for game_over
        self.consecutive_pass = 0
        for x in range(rows):
            self.__board.append([])
            for _ in range(cols):
                self.__board[x].append(None)
        self.__message = 'This is default value for message'

        #attributes I am experimenting with for undo()
        self.moves = {
            0 : self.copy_board()
        }
        self.move_num = 1

        # previous board's default value needs to have the index but needs to have something in it that would never appear
        self.previous_board = [['value that would never appear']]

        self.cant_play = []
        self.checked = []
        self.last_placed = None
        self.breakout = False
        self.visited = []

    # Properties
    @property
    def nrows(self):
        """
        Property get method for nrows.

        Returns:
            Int: number of rows
        """
        return self.__nrows
    @property
    def ncols(self):
        '''
        Property get method for ncols.

        Returns:
            Int: number of collumns
        '''
        return self.__ncols
    @property
    def current_player(self):
        '''
        Property get method for current_player

        Returns:
            GamePlayer: The Current player
        '''
        return self.__current_player
    @property
    def board(self):
        '''
        Property get method for board

        Returns:
            List: returns the Board
        '''
        return self.__board
    # @board.setter
    # def board(self, board): #COMMENT THIS OUT IF SUMBITTING!!! :)
    #     self.__board = board
    @property
    def message(self):
        '''
        Property get method for message

        Returns:
             str: returns the message
        '''
        return self.__message
    @message.setter
    def message(self, mes):
        '''
        Property setter for message

        Raises:
             TypeError: if mes is not a str
        '''
        if not isinstance(mes, str):
            raise TypeError
        self.__message = mes

    def piece_at(self, pos):
        """
        Returns the piece's position on the board and checks if the position
        is out of bounds.

        Returns:
            GamePiece: returns the game piece at the specified position
        Raises:
            TypeError: if pos is not a Position object
            ValueError: if specified pos is not within range of the board
        """
        # implemented the check from placeble
        if not isinstance(pos, Position):
            raise TypeError
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise ValueError('Out of bounds.')
        #print(f"Getting piece at: ({pos.row}, {pos.col})")
        return self.__board[pos.row][pos.col]

    #should be working, but we need is_valid_placement to work first
    def set_piece(self, pos, piece = None):
        """
        Sets the piece's position on the board.

        Raises:
            ValueError: if specified position is not within bounds
        """
        if not isinstance(pos, Position):
            raise TypeError
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise ValueError('Out of bounds.')
        if self.is_valid_placement(pos, piece):
            self.last_placed = [pos.row, pos.col]
            self.__board[pos.row][pos.col] = piece
            self.moves[self.move_num] = self.copy_board() #creates the previous board onto the moves dict
            # self.previous_board = self.moves.pop(self.move_num)
            self.move_num += 1 #updates the number of moves done
            self.consecutive_pass = 0

            # print(f"Setting piece at ({pos.row}, {pos.col})")


    def set_next_player(self):
        """
        Changes the current player to the next, and thus, changes turn.
        """
        #two attributes
        #if one, do the other
        if self.__current_player.player_color == self.__player1.player_color:
            self.__current_player = self.__player2
        #same
        elif self.__current_player.player_color == self.__player2.player_color:
            self.__current_player = self.__player1
        # print('This is current player set_next', self.__current_player)
        # print('Printing player1', self.__player1)
        # print('============')
        # print('Printing player2', self.__player2)
        # print(id(self.__current_player), id(self.__player1), id(self.__player2))

        # else:
        #     self.__current_player = GamePlayer(PlayerColors.BLACK)
        # player1 = GamePlayer(PlayerColors.BLACK)
        # player2 = GamePlayer(PlayerColors.WHITE)
        # self.__current_player = player1
        # opponent_player = player2

    #working
    def pass_turn(self):
        """
        Skips the player's turn and updates the player's skip_count.
        """
        self.set_next_player()
        self.__current_player.skip_count += 1
        self.consecutive_pass += 1
        print('This is current player, method pass_turn',self.__current_player)

    #should be working, but we need is_valid_placement to work first
    def is_game_over(self):
        """
        Returns True if two consecutive skips are made.
        """

        if self.consecutive_pass == 2:
            return True
        else:
            return False
        # else:
        #     self.pass_count = 0
        # if self.__current_player.skip_count >= 2:
        #     return True
        # return False

    #DOESN'T WORK yet
    def is_valid_placement(self, pos, piece):
        '''
        Uses previous parent class is_valid_placement if returns tru then checks
        the position is in cant play list, if the position would revert to a previous
        board.

        Returns:
            bool: True if the placement is valid false if the placement is not valid
        '''
        # if piece is None:
        #     self.message = 'Invalid placement'
        #     return False
        if not piece.is_valid_placement(pos, self.board):
            self.message = ('Invalid Placement: Either not within bounds,\n'
                            'or piece is already surrounded by opponent pieces')
            return False

        temp_board = self.copy_board()

        #temp_board = self.board
        # print(f'This is temp board: {temp_board}')
        # print('=======')
        # print(f'This is board:{self.board}')

        #adds the current piece being considered if it is valid
        temp_board[pos.row][pos.col] = piece

        # uncomment line under if you want to see the 2 values being compared
        # print(f'\n\nprevious:{self.previous_board}\nwill be:{temp_board}\n\n')

        if [pos.row, pos.col] in self.cant_play:
            return False

        #compares all the elements in the previous board verifying that
        # for i in self.moves.values():
        for row in range(len(self.previous_board)):
            for col in range(len(self.previous_board)):
                if self.previous_board[row][col] != temp_board[row][col]:
                    return True #will return true for the first option when the 2nd option could have the same board
        self.message = 'can\'t play would result in previous board state'
        return False
        # if temp_board == self.previous_board:
        #     return False

    def capture(self):
        '''
        Runs bucket_check() for the current_player and increments their capture_count by the result
        '''
        def capture_check(row, col, visited, potential_count, capturing_color=None):
            # captured_color
            # piece_at_position = g.board[row][col]
            if self.breakout:
                # print('breaking out')
                return 0
            if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):  # out of board
                # print('Out of bounds')
                return potential_count
            piece_at_position = self.board[row][col]
            # print(
            #     f'Position: R{row}, C{col}, truth {piece_at_position != capturing_color}, visited{visited}, capturing_color{capturing_color} ')
            if [row, col] in visited:  # already checked
                # print('Position already checked')
                return potential_count
            if piece_at_position == capturing_color:  # if it runs into the color that is trying to surround returns to call function
                #     # print(f'Position: R{row}, C{col}, truth {piece_at_position != color}, visited{visited}, color{color} ')
                # print('ran into surrounding color')
                return potential_count

            if piece_at_position is None:
                self.breakout = True
                potential_count = 0

            potential_count += 1
            visited.append([row, col])


            potential_count = capture_check(row + 1, col, visited, potential_count, capturing_color)
            potential_count = capture_check(row - 1, col, visited, potential_count, capturing_color)
            potential_count = capture_check(row, col + 1, visited, potential_count, capturing_color)
            potential_count = capture_check(row, col - 1, visited, potential_count, capturing_color)
            return potential_count

        color = self.board[self.last_placed[0]][self.last_placed[1]]
        self.breakout = False
        self.visited = []
        down = capture_check(self.last_placed[0] + 1, self.last_placed[1], self.visited, 0, color)
        # print(f'\n\n{self.current_player.player_color}:{down}\n\n')
        self.current_player.capture_count += down
        if down > 0:
            for cords in self.visited:
                self.board[cords[0]][cords[1]] = None
                self.cant_play.append(cords)
        self.breakout = False
        self.visited = []

        up = capture_check(self.last_placed[0] - 1, self.last_placed[1], self.visited, 0, color)
        # print(f'\n\n{self.current_player.player_color}:{up}\n\n')
        self.current_player.capture_count += up
        if up > 0:
            for cords in self.visited:
                self.board[cords[0]][cords[1]] = None
                self.cant_play.append(cords)
        self.breakout = False
        self.visited = []

        right = capture_check(self.last_placed[0], self.last_placed[1] + 1, self.visited, 0, color)
        # print(f'\n\n{self.current_player.player_color}:{right}\n\n')
        self.current_player.capture_count += right
        if right > 0:
            for cords in self.visited:
                self.board[cords[0]][cords[1]] = None
                self.cant_play.append(cords)
        self.breakout = False
        self.visited = []

        left = capture_check(self.last_placed[0], self.last_placed[1] - 1, self.visited, 0, color)
        # print(f'\n\n{self.current_player.player_color}:{left}\n\n')
        self.current_player.capture_count += left
        if left > 0:
            for cords in self.visited:
                self.board[cords[0]][cords[1]] = None
                self.cant_play.append(cords)
        self.breakout = False
        self.visited = []

        # print(f'\n{self.current_player.player_color}:{self.current_player.capture_count}\n')



    def calculate_score(self):
        '''
        Calculates the score between the 2 players and returns them in a list

        Returns:
            list: returns score for both players Ex: [Black_score, White_score]
        '''
        white = 0
        black = 0
        for row in self.board:
            for place in row:
                if place == GamePiece(PlayerColors.BLACK):
                    black += 1
                elif place == GamePiece(PlayerColors.WHITE):
                    white += 1
        if self.current_player == GamePlayer(PlayerColors.BLACK):
            black += self.current_player.capture_count
            self.set_next_player()
            white += self.current_player.capture_count
            self.set_next_player()
        elif self.current_player == GamePlayer(PlayerColors.WHITE):
            white += self.current_player.capture_count
            self.set_next_player()
            black += self.current_player.capture_count
            self.set_next_player()
        return [black, white]

    def undo(self):
        '''
        Undoes the most recent made move on the board

        Raises:
            UndoException: Raised when there is nothing to undo
        '''
        if not self.moves or self.move_num == 1: #raises UndoException when out of undos or when its the very first turn
            raise UndoException('Nothing to Undo')

        # takes the previous move_num (the keys for moves) which gives the board 1 move earlier
        # the for loop is copying self.moves[self.move_num-1]'s board to self.board without a setter
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                self.board[row][col] = self.moves[self.move_num-2][row][col]

        self.set_next_player() #switches the player turn to the other.
        self.previous_board = self.moves[self.move_num-1] #keeping previous hand is purely for the is_valid_placement check.
        # but since its a pop its also for removing it
        self.move_num -= 1 #brings the current move_num down 1

    #this way of copying board makes so that the GamePiece references are the same value
    def copy_board(self):
        '''
        makes a copy of the board making sure to keep the same gamepiece references

        Returns:
            List: returns the exact same current value of the board
        '''
        b = []
        for row in self.board:
            updated_row = []
            for square in row:
                updated_row.append(square)
            b.append(updated_row)
        return b

    # def take_empty(self, color): #seperate from capture() used for when pieces surround an empty space
    #     '''
    #
    #     '''
    #     open_spots = []
    #     potential_count = 0
    #     surround = []
    #     for row in range(len(self.board)):
    #         for col in range(len(self.board[row])):
    #             if self.board[row][col] is None:
    #                 open_spots.append([row, col])
    #                 potential_count += 1
    #     for i in open_spots:
    #         r = i[0]
    #         c = i[1]
    #         adjacent = [[1 + r, c], [-1 + r, c], [r, 1 + c], [r, -1 + c]]
    #         for adj in adjacent:
    #             if adj[0] < 0 or adj[1] < 0 or adj[0] >= len(self.board) or adj[1] >= len(self.board[0]):
    #                 pass
    #             else:
    #                 if self.board[adj[0]][adj[1]] is None:
    #                     if self.board[adj[0]][adj[1]] not in open_spots:
    #                         open_spots.append([adj[0], adj[1]])
    #                 elif self.board[adj[0]][adj[1]] == color:
    #                     surround.append([r, c])
    #                 else:
    #                     open_spots.remove([r, c]) #This may cause an error as your removing something from a list while iteration through them

        # bucket = []
        # potential_count = 0
        # possible_opponents = []
        # not_surrounded_pieces = []
        # for row in range(len(self.board)):
        #     for col in range(len(self.board[row])):
        #         if self.board[row][col] == None:
        #             bucket.append([row, col])
        #             potential_count += 1
        # for i in bucket:
        #     r = i[0]
        #     c = i[1]
        #     adjacent = [[1+r, c], [-1+r, c], [r, 1+c], [r, -1+c]]
        #     for adj in adjacent:
        #         if adj[0] < 0 or adj[1] < 0 or adj[0] >= len(self.board) or adj[1] >= len(self.board[0]):
        #             pass
        #         else:
        #             if self.board[adj[0]][adj[1]] == None:
        #                 if [adj[0], adj[1]] not in bucket:
        #                     bucket.append([adj[0], adj[1]])
        #             elif self.board[adj[0]][adj[1]] != color:
        #                 if [r, c] not in not_surrounded_pieces:
        #                     not_surrounded_pieces.append([r, c])
        #                     potential_count -= 1
        #             elif self.board[adj[0]][adj[1]] == color:
        #                 possible_opponents.append(adj)
        # for piece in not_surrounded_pieces:
        #     bucket.remove(piece) #removes from bucket
        # for piece in not_surrounded_pieces:
        #     r = piece[0]
        #     c = piece[1]
        #     adjacent = [[1+r, c], [-1+r, c], [r, 1+c], [r, -1+c]]
        #         #then needs to remove the neighbors of this piece
        #     for i in adjacent:
        #         if i in bucket:
        #             return 0
        #                 # needs_recheck.append(piece)
        #                 #appends any piece that is not surrounded and connected to main blob
        #     for i in adjacent:
        #         if i in possible_opponents:
        #             possible_opponents.remove(i)
        #         # for i in adjacent:
        #         #     if i in possible_opponents and not dont_remove_bc_connects:
        #         #         possible_opponents.remove(i)
        #         #     elif dont_remove_bc_connects:
        #         #         if i
        #
        #
        #     # print(f'\nopponents: {possible_opponents}\n')
        # for i in possible_opponents:
        #     if self.board[i[0]][i[1]] is None or self.board[i[0]][i[1]] != color:
        #         return 0 #gets out of the method if they aren't surrounded
        # for i in bucket:
        #     self.board[i[0]][i[1]] = None
        #     self.cant_play.append(i)
        # return potential_count





g = GoModel()
g.calculate_score()
# piece1 = GamePiece(PlayerColors.WHITE)
# piece2 = GamePiece(PlayerColors.BLACK)
# pos1 = Position(2,2)
# pos2 = Position(2,3)
# pos3 = Position(3,2)
# pos4 = Position(3,3)

# g.set_piece(pos1, piece1)
# g.set_piece(pos2, piece1)
# g.set_piece(pos3, piece1)
# g.set_piece(pos4, piece1)

# black1 = Position(1,2)
# black2 = Position(1,3)
#
# black3 = Position(2,4)
# black4 = Position(3,4)
#
# black5 = Position(4,3)
# black6 = Position(4,2)
#
# black7 = Position(3,1)
# black8 = Position(2,1)
#
# g.set_piece(black1, piece2)
# g.set_piece(black2, piece2)
# g.set_piece(black3, piece2)
# g.set_piece(black4, piece2)
# g.set_piece(black5, piece2)
# g.set_piece(black6, piece2)
# g.set_piece(black7, piece2)
# g.set_piece(black8, piece2)

# test = Position(5,5)
# g.set_piece(test, piece1)


# for i in g.board:
#     print(i)
#print(f'\n{g.take_empty(GamePiece(PlayerColors.BLACK))}\n')
# g.capture()
# for i in g.board:
#     print(i)

#g.capture()