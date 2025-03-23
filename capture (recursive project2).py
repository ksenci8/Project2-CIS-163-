from go_model import GoModel
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position


def capture(g, row, col, visited, potential_count, color=None):
    if row < 0 or col < 0 or row >= len(g.board) or col >= len(g.board[0]):  # out of board
        print('out of board')
        return potential_count
    if [row, col] in visited:  # already checked
        print('hit already checked')
        return potential_count
    if color and g.board[row][
        col] != color:  # if it runs into the color that is trying to surround returns to call function
        if [row, col] in visited:
            print('ran into surrounding color')
            return potential_count

    potential_count += 1
    visited.append([row, col])

    print(f'Position: R{row}, C{col}, truth {g.board[row][col] != color}, visited{visited}, color{color} ')

    potential_count = capture(g, row + 1, col, visited, potential_count, color)
    potential_count = capture(g, row - 1, col, visited, potential_count, color)
    potential_count = capture(g, row, col + 1, visited, potential_count, color)
    potential_count = capture(g, row, col - 1, visited, potential_count, color)

    return potential_count


# g = GoModel()
# piece1 = GamePiece(PlayerColors.WHITE)
# piece2 = GamePiece(PlayerColors.BLACK)
# pos1 = Position(3, 3)
# g.set_piece(pos1, piece2)
# capture(g, pos1.row, pos1.col, [], 0,  piece1)

# print(capture(g, pos1.row+1, pos1.col, [], 0, run_into, piece1))
# print(capture(g, pos1.row-1, pos1.col, [], 0, run_into, piece1))
# print(capture(g, pos1.row, pos1.col+1, [], 0, run_into, piece1))
# print(capture(g, pos1.row, pos1.col-1, [], 0, run_into, piece1))

# g = GoModel()
# piece1 = GamePiece(PlayerColors.WHITE)
# piece2 = GamePiece(PlayerColors.BLACK)
# pos1 = Position(3, 3)
# g.set_piece(pos1, piece2)
# capture(g, pos1.row, pos1.col, [], 0,  piece1)
g = GoModel()

# Create white and black pieces
white = GamePiece(PlayerColors.WHITE)
black = GamePiece(PlayerColors.BLACK)

# Place a small black group (2 stones)
black_pos1 = Position(3, 3)
black_pos2 = Position(3, 4)
g.set_piece(black_pos1, black)
g.set_piece(black_pos2, black)

# Surround the black group with white stones
# Around (3, 3)
g.set_piece(Position(2, 3), white)
g.set_piece(Position(3, 2), white)
g.set_piece(Position(4, 3), white)

# Around (3, 4)
g.set_piece(Position(2, 4), white)
g.set_piece(Position(3, 5), black)
g.set_piece(Position(4, 4), white)


# The two black stones share one liberty at (3, 2), which is now occupied.

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

# Attempt to capture starting from one of the black stones
captured = capture(g, black_pos1.row, black_pos1.col, [], 0, white)

print("Captured:", captured)









# run_into = [[0, 1], [1,0], [2,1], [1,2]]
# g = GoModel()
# piece1 = GamePiece(PlayerColors.WHITE)
# piece2 = GamePiece(PlayerColors.BLACK)
# pos1 = Position(1, 1)
# g.set_piece(pos1, piece2)
# # print(capture(g, pos1.row, pos1.col, [], 0, run_into, piece1))
#
# print(capture(g, pos1.row+1, pos1.col, [], 0, run_into, piece1))
# print(capture(g, pos1.row-1, pos1.col, [], 0, run_into, piece1))
# print(capture(g, pos1.row, pos1.col+1, [], 0, run_into, piece1))
# print(capture(g, pos1.row, pos1.col-1, [], 0, run_into, piece1))



