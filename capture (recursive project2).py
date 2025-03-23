from go_model import GoModel
from game_player import GamePlayer
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position


def capture(g, row, col,  visited, potential_count, run_into, color= None, first = True, first_ran = True):
    if row < 0 or col < 0 or row >= len(g.board) or col >= len(g.board[0]): #out of board
        print('out of board')
        return potential_count
    if [row, col] in run_into: #exit out of recursion because its run into the other recursion Ex: r1 clashed with r2
        if first_ran:
            first_ran = False
            pass
        else:
            print('ran into')
            return 0
    if [row, col] in visited: #already checked
        print('hit already checked')
        return potential_count
    if color and g.board[row][col] != color: #if it runs into the color that is trying to surround returns to call function
        if first:
            first = False
            pass
        else:
            if [row, col] in visited:
                print('ran into surrounding color')
                return potential_count

    potential_count += 1
    visited.append([row, col])

    potential_count = capture(g, row + 1, col, visited, potential_count, run_into, color, first, first_ran)
    potential_count = capture(g, row - 1, col, visited, potential_count, run_into, color, first, first_ran)
    potential_count = capture(g, row, col + 1, visited, potential_count, run_into, color, first, first_ran)
    potential_count = capture(g, row, col - 1, visited, potential_count, run_into, color, first, first_ran)
    print(f'Position: {row}, {col}')
    return potential_count

run_into = [[0, 1], [1,0], [2,1], [1,2]]
g = GoModel()
piece1 = GamePiece(PlayerColors.WHITE)
piece2 = GamePiece(PlayerColors.BLACK)
pos1 = Position(1, 1)
g.set_piece(pos1, piece2)
# print(capture(g, pos1.row, pos1.col, [], 0, run_into, piece1))

print(capture(g, pos1.row+1, pos1.col, [], 0, run_into, piece1))
print(capture(g, pos1.row-1, pos1.col, [], 0, run_into, piece1))
print(capture(g, pos1.row, pos1.col+1, [], 0, run_into, piece1))
print(capture(g, pos1.row, pos1.col-1, [], 0, run_into, piece1))