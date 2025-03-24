from go_model import GoModel
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position


def capture(g, row, col, visited, potential_count, capturing_color = None):
    #captured_color
    # piece_at_position = g.board[row][col]
    global breakout
    if breakout:
        print('breaking out')
        return 0
    if row < 0 or col < 0 or row >= len(g.board) or col >= len(g.board[0]):  # out of board
        print('Out of bounds')
        return potential_count
    piece_at_position = g.board[row][col]
    print(f'Position: R{row}, C{col}, truth {piece_at_position != capturing_color}, visited{visited}, capturing_color{capturing_color} ')
    if [row, col] in visited:  # already checked
        print('Position already checked')
        return potential_count
    if piece_at_position == capturing_color:  # if it runs into the color that is trying to surround returns to call function
    #     # print(f'Position: R{row}, C{col}, truth {piece_at_position != color}, visited{visited}, color{color} ')
        print('ran into surrounding color')
        return potential_count


    # liberties = 0
    # for col_dir, row_dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  #Directions: 4, tuples
    #     new_row = row + row_dir
    #     new_col = col + col_dir
    #     if 0 <= new_row < len(g.board) and 0 <= new_col < len(g.board[0]):
    #         print('in range of board')
    #         if g.board[new_row][new_col] is None or g.board[new_row][new_col] == capturing_color:
    #             print('if empty or not surrounding color')
    #             liberties += 1

    if piece_at_position is None:
        breakout = True
        potential_count = 0




    # if liberties > 0:
    #     return potential_count

    potential_count += 1
    visited.append([row, col])


    # print(f'Checking below R{row}, C{col}')
    potential_count = capture(g, row + 1, col, visited, potential_count, capturing_color)
    # print(f'Checking below R{row}, C{col}')
    potential_count = capture(g, row - 1, col, visited, potential_count, capturing_color)
    potential_count = capture(g, row, col + 1, visited, potential_count, capturing_color)
    # print(f'Checking right R{row}, C{col}')
    potential_count = capture(g, row, col - 1, visited, potential_count, capturing_color)
    # print(f'Checking left R{row}, C{col}')
    # if liberties > 0:
    #     return potential_count
    return potential_count

g = GoModel()


#TWO BLACK STONES ARE CAPTURED

# # Create white and black pieces
# white = GamePiece(PlayerColors.WHITE)
# black = GamePiece(PlayerColors.BLACK)

# # Place a small black group (2 stones)
# black_pos1 = Position(3, 3)
# black_pos2 = Position(3, 4)
# g.set_piece(black_pos1, black)
# g.set_piece(black_pos2, black)
#
# # Surround the black group with white stones
# # Around (3, 3)
# g.set_piece(Position(2, 3), white)
# g.set_piece(Position(3, 2), white)
# g.set_piece(Position(4, 3), white)
#
# # Around (3, 4)
# g.set_piece(Position(2, 4), white)
# g.set_piece(Position(3, 5), white)
# g.set_piece(Position(4, 4), white)

# The two black stones share one liberty at (3, 2), which is now occupied.

white = GamePiece(PlayerColors.WHITE)
black = GamePiece(PlayerColors.BLACK)
black_pos1 = Position(3, 3)
black_pos2 = Position(3, 4)
#
# g.set_piece(black_pos1, black)
# g.set_piece(black_pos2, black)

# Surround the black group with white stones but leave a liberty (empty spot at (2, 2))
# g.set_piece(Position(2, 3), white)
# g.set_piece(Position(3, 2), white)
# g.set_piece(Position(4, 3), white)
#
# g.set_piece(Position(2, 4), white)
# g.set_piece(Position(3, 5), white)
# g.set_piece(Position(4, 4), white)

# Add liberty at (2, 2) to prevent capture
# g.set_piece(Position(2, 3), None)  # Empty spot, providing a liberty

# Capture test setup
# visited = []
# potential_count = 0
# color_to_capture = 'B'  # Color we want to capture (black)
# start_row = 3
# start_col = 3


g.board = [
[None,None,None,white,None,None,],
[None,None,white,black,white,None],
[None,None,None,white,None,None],
[None,None,white,black,white,None],
[None,None,None,white,None,None],
[None,None,None,None,None,None]
]
def print_board(g, size=6):
    print("   " + " ".join(f"{c}" for c in range(size)))
    for r in range(size):
        row_str = f"{r}  "
        for c in range(size):
            piece = g.piece_at(Position(r, c))
            if piece is None:
                row_str += ". "
            elif piece.color == PlayerColors.BLACK:
                row_str += "B "
            elif piece.color == PlayerColors.WHITE:
                row_str += "W "
        print(row_str)

print_board(g)



breakout = False
# Attempt to capture starting from one of the black stones
captured = capture(g, black_pos1.row, black_pos1.col, [], 0, white)
breakout = False
print("Captured:", captured)
#last pieces that should be placed should be white
#row and col have to be black, and vice versa.