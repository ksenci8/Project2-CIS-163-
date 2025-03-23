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
    pass

class GoModel:
    #constructor
    def __init__(self, rows = 6, cols = 6):
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
    #I know board.setter is not specified in the project, but I created for usage in undo()
    # @board.setter
    # def board(self, board):
    #     self.__board = board
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
        # implemented the check from placeble
        if not isinstance(pos, Position):
            raise TypeError
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise ValueError('Out of bounds.')
        print(f"Getting piece at: ({pos.row}, {pos.col})")
        return self.__board[pos.row][pos.col]

    #should be working, but we need is_valid_placement to work first
    def set_piece(self, pos, piece = None):
        """
        Sets the piece's position on the board.
        """
        # if not isinstance(piece, GamePiece):
        #     raise TypeError
        # if not isinstance(pos, Position):
        #     raise TypeError
        if (pos.row < 0 or pos.row >= self.__nrows) or (pos.col < 0 or pos.col >= self.__ncols):
            raise ValueError('Out of bounds.')
        if self.is_valid_placement(pos, piece):
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
        for i in self.moves.values():
            for row in range(len(i)):
                for col in range(len(i)):
                    if i[row][col] != temp_board[row][col]:
                        return True
        return False
        # if temp_board == self.previous_board:
        #     return False

    def capture(self):
        print('\n\nentering capture\n\n')
        def bucket_check(color):
            bucket = []
            potential_count = 0
            possible_opponents = []
            not_surrounded_pieces = []
            remove_pieces = []
            #checked = []
            #notes all of the cordinates of the pieces of the specified color
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] != None and self.board[row][col] == color:
                        bucket.append([row, col])
                        potential_count += 1
            for i in bucket: #this for loop looks at all of the adjacent spots to all the pieces in bucket
                r = i[0]
                c = i[1]
                adjacent = [[1+r, c], [-1+r, c], [r, 1+c], [r, -1+c]]
                for adj in adjacent:
                    if adj[0] < 0 or adj[1] < 0 or adj[0] >= len(self.board) or adj[1] >= len(self.board[0]): #cuts off space if off board
                        pass
                    else:
                        # if self.board[adj[0]][adj[1]] == color: #adds any piece that is the same color and not already in the bucket
                        #     if [adj[0], adj[1]] not in bucket:
                        #         bucket.append([adj[0], adj[1]])
                        if self.board[adj[0]][adj[1]] is None: #if a piece has None as an adjacent it's not surrounded so it gets added to not_surrounded_pieces
                            if [r, c] not in not_surrounded_pieces:
                                not_surrounded_pieces.append([r, c])
                                potential_count -= 1
                        elif self.board[adj[0]][adj[1]] != color: #creates a list of possible_opponenets pieces that might be surrounding
                            possible_opponents.append(adj)
            for piece in not_surrounded_pieces: #now we cycle through not_surrounded removing them from the bucket
                for i in bucket: #just a for loop here to verify that I remove it all even if there are duplicates
                    if i == piece:
                        bucket.remove(piece) #removes from bucket

            for piece in not_surrounded_pieces: #now we cycle through them again and if the not_surrounded_pieces is connected
                # to one of the pieces in bucket it removes that piece from bucket as it can't be surrounded if its connected
                #to a piece that has a None as a neighbor
                r = piece[0]
                c = piece[1]
                adjacent = [[1+r, c], [-1+r, c], [r, 1+c], [r, -1+c]]
                #then needs to remove the neighbors of this piece
                for i in adjacent:
                    if i in bucket:
                        bucket.remove([i[0], i[1]]) #Was failing here
                        potential_count -= 1

                for i in adjacent: #removes any possible opponents that is near not_surrounded
                    if i in possible_opponents:
                        possible_opponents.remove(i)
            for i in bucket: #This for loop explores all the neighbors that are the same color. if any of them are connected to
                r = i[0]
                c = i[1]
                adjacent = [[1+r, c], [-1+r, c], [r, 1+c], [r, -1+c]]
                for adj in adjacent:
                    if self.board[adj[0]][adj[1]] == color:
                        if adj not in bucket:
                            bucket.append(adj)
                            remove_pieces.append(adj)
                    if self.board[adj[0]][adj[1]] is None:
                        return 0
            for i in remove_pieces:
                if i in bucket:
                    bucket.remove(i)


            #print(f'BUCKET: {bucket}')
            if len(bucket) == 1: #had an error with single capture so it runs seperately if the bucket is just 1 piece
                r = bucket[0][0]
                c = bucket[0][1]
                adjacent = [[1 + r, c], [-1 + r, c], [r, 1 + c], [r, -1 + c]]
                for i in adjacent:
                    if self.board[i[0]][i[1]] == (color or None):
                        return 0
                self.board[r][c] = None
                self.cant_play.append([r, c])
                return 1

            #print(f'\nopponents: {possible_opponents} {color}\n')

            for i in possible_opponents: #finally cycles through possible opponents returning 0 if any of the possible_opponent
                # places are empty or the same color
                if self.board[i[0]][i[1]] is None or self.board[i[0]][i[1]] == color:
                    return 0 #gets out of the method if they aren't surrounded
            for i in bucket: #cycles through bucket making them empty spaces and appending them to cant_play
                self.board[i[0]][i[1]] = None
                self.cant_play.append(i)
            return potential_count

        self.__player1.capture_count = self.__player1.capture_count + bucket_check(GamePiece(PlayerColors.WHITE))

        self.__player2.capture_count = self.__player2.capture_count + bucket_check(GamePiece(PlayerColors.BLACK))
        print(self.__player1.capture_count)
        print(self.__player2.capture_count)
        print(self.board)

    def calculate_score(self):
        pass

    def undo(self):
        if not self.moves or self.move_num == 1: #raises UndoException when out of undos or when its the very first turn
            raise UndoException('Nothing to Undo')

        # takes the previous move_num (the keys for moves) which gives the board 1 move earlier
        # the for loop is copying self.moves[self.move_num-1]'s board to self.board without a setter
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                self.board[row][col] = self.moves[self.move_num-2][row][col]

        self.set_next_player() #switches the player turn to the other.
        self.previous_board = self.moves.pop(self.move_num-1) #keeping previous hand is purely for the is_valid_placement check.
        # but since its a pop its also for removing it
        self.move_num -= 1 #brings the current move_num down 1

    #this way of copying board makes so that the GamePiece references are the same value
    def copy_board(self):
        b = []
        for row in self.board:
            updated_row = []
            for square in row:
                updated_row.append(square)
            b.append(updated_row)
        return b

    def take_empty(self, color): #seperate from capture() used for when pieces surround an empty space
        open_spots = []
        potential_count = 0
        surround = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] is None:
                    open_spots.append([row, col])
                    potential_count += 1
        for i in open_spots:
            r = i[0]
            c = i[1]
            adjacent = [[1 + r, c], [-1 + r, c], [r, 1 + c], [r, -1 + c]]
            for adj in adjacent:
                if adj[0] < 0 or adj[1] < 0 or adj[0] >= len(self.board) or adj[1] >= len(self.board[0]):
                    pass
                else:
                    if self.board[adj[0]][adj[1]] is None:
                        if self.board[adj[0]][adj[1]] not in open_spots:
                            open_spots.append([adj[0], adj[1]])
                    elif self.board[adj[0]][adj[1]] == color:
                        surround.append([r, c])
                    else:
                        open_spots.remove([r, c]) #This may cause an error as your removing something from a list while iteration through them

    # def add_neighbors(self, piece, color, checked= []):
    #     print('entering function')
    #     r = piece[0]
    #     c = piece[1]
    #     adjacent = [[1 + r, c], [-1 + r, c], [r, 1 + c], [r, -1 + c]]
    #     if piece in checked:
    #         return
    #     checked.append([piece[0], piece[1]])
    #     for adj in adjacent:
    #         if self.board[adj[0]][adj[1]] == color:
    #             print('entering recursion')
    #             self.add_neighbors([adj[0], adj[1]], color, checked)
    #         if self.board[adj[0]][adj[1]] is None:
    #             print('should be working')
    #             return True
    #     print('returning false for some reason')
    #     return


# g = GoModel()
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