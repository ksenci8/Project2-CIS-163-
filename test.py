# testing for Project 2
import unittest
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position
from go_model import GoModel, UndoException
from game_piece import GamePiece
from game_player import GamePlayer

class TestGoStep2(unittest.TestCase):
    def test_check_if_valid(self):
        g = GamePiece(PlayerColors.BLACK)
        board = [
        [None, GamePiece(PlayerColors.BLACK), None],
        [GamePiece(PlayerColors.WHITE), GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)],
        [None, GamePiece(PlayerColors.BLACK), None]
           ]
        #Placement valid (not surrounded by opponent)
        self.assertTrue(g.is_valid_placement(Position(0,0), board))
        #Placement not valid (surrounded)
        self.assertFalse(g.is_valid_placement(Position(1,1), board))
        #Placement valid (not surrounded by opponent)
        self.assertTrue(g.is_valid_placement(Position(2, 2), board))

    def test_out_of_bounds(self):
        g = GamePiece(PlayerColors.BLACK)
        board = [
            [None, GamePiece(PlayerColors.BLACK), None],
            [GamePiece(PlayerColors.WHITE), GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)],
            [None, GamePiece(PlayerColors.BLACK), None]
        ]
        self.assertFalse(g.is_valid_placement(Position(-1,-5), board))
        self.assertFalse(g.is_valid_placement(Position(-1,0), board))
        self.assertFalse(g.is_valid_placement(Position(10,5), board))

    def test_edge_valid(self):
        g = GamePiece(PlayerColors.BLACK)
        board = [
        [None, GamePiece(PlayerColors.BLACK), None],
        [GamePiece(PlayerColors.WHITE), GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)],
        [None, GamePiece(PlayerColors.BLACK), None]
    ]
        #valid
        self.assertTrue(g.is_valid_placement(Position(0,2), board))


    def test_edge_invalid(self):
        g = GamePiece(PlayerColors.BLACK)
        board = [
            [None, GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.BLACK)],
            [GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)],
            [None, GamePiece(PlayerColors.BLACK), None]
        ]
        #invalid
        self.assertFalse(g.is_valid_placement(Position(0,2), board))
        board = [
            [None, GamePiece(PlayerColors.BLACK), None],
            [GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)],
            [None, GamePiece(PlayerColors.BLACK), GamePiece(PlayerColors.WHITE)]  #Space empty at(2,0)
        ]
        self.assertTrue(g.is_valid_placement(Position(2,0), board))

    def test__eq__(self):
        piece1 = GamePiece(PlayerColors.BLACK)
        piece2 = GamePiece(PlayerColors.BLACK)
        piece3 = GamePiece(PlayerColors.WHITE)

        #Should be
        self.assertEqual(piece1, PlayerColors.BLACK)
        #Should not be equal
        self.assertNotEqual(piece3, PlayerColors.BLACK)
        #Invalid comparison
        self.assertNotEqual(piece1, 4)

class TestGoStep3(unittest.TestCase):
    def constructor(self):
        p = GamePlayer()
        with self.assertRaises(TypeError):
            p.capture_count('hello')
        with self.assertRaises(TypeError):
            p.skip_count(kjk)
        with self.assertRaises(TypeError):
            p.player_color('black')


class TestGoStep4(unittest.TestCase):
    def setUp(self):
        self.game = GoModel(rows = 6, cols = 6)
        self.gp = GamePlayer(PlayerColors.BLACK)


    def test_initial_board_size(self):
        self.assertEqual(len(self.game._GoModel__board), 6)

    def test_board_is_list(self):
        self.assertIsInstance(self.game._GoModel__board, list)

    def test_move_num_starts_at_one(self):
        self.assertEqual(self.game.move_num, 1)

    def test_pass_turn_switch_player(self):
        # Pass turn once, should switch from black to white
        self.game.pass_turn()
        self.assertEqual(self.game.current_player.player_color, PlayerColors.WHITE)

    def test_pass_turn_multiple_switches(self):
        #Pass turn multiple times
        self.game.pass_turn()
        self.assertEqual(self.game.current_player.player_color, PlayerColors.WHITE)

        self.game.pass_turn()  #white to black
        self.assertEqual(self.game.current_player.player_color, PlayerColors.BLACK)

        self.game.pass_turn()  #black to white
        self.assertEqual(self.game.current_player.player_color, PlayerColors.WHITE)

    def test_skip_count_increment(self):
        self.game.pass_turn()
        self.assertEqual(self.game.current_player.skip_count, 1)

        #Pass turn again, skip count for black (next player) should increment
        self.game.pass_turn()
        self.assertEqual(self.game.current_player.skip_count, 1)

        #Pass turn again, white skip count should now be 2
        self.game.pass_turn()
        self.assertEqual(self.game.current_player.skip_count, 2)

    def test_consecutive_pass_increment(self):
        self.assertEqual(self.game.consecutive_pass, 0)

        #Pass turn, should increment to 1
        self.game.pass_turn()
        self.assertEqual(self.game.consecutive_pass, 1)

        self.game.pass_turn()
        self.assertEqual(self.game.consecutive_pass, 2)

    def test_consecutive_pass_reset_on_set_piece(self):
        #Consecutive pass increments on passing
        self.game.pass_turn()
        self.game.pass_turn()
        self.assertEqual(self.game.consecutive_pass, 2)
    def test_is_valid_placement(self):
        with self.assertRaises(TypeError):
            self.game.is_valid_placement('jdjadjadh')
    def test_is_game_over(self):
        self.game.pass_turn()
        self.game.pass_turn()
        self.assertTrue(self.game.is_game_over())
        self.game.consecutive_pass = 1
        self.assertFalse(self.game.is_game_over())

        #Setting a piece should reset consecutive_pass to 0
        self.game.set_piece(Position(0, 0), GamePiece(PlayerColors.BLACK))
        self.assertEqual(self.game.consecutive_pass, 0)


    def test_copy_board_creates_new_list(self):
        copied_board = self.game.copy_board()
        self.assertIsInstance(copied_board, list)


    # def test_is_valid_placement_true(self):
    #     self.assertTrue(self.game.is_valid_placement(self.piece, (4, 4)))

    def test_undo_raises_exception(self):
        with self.assertRaises(UndoException):
            self.game.undo()
    # def test_set_piece(self):
    #     game = GoModel(6,6)
    #     piece = GamePiece(PlayerColors.WHITE)
    #     pos = Position(1,1)
    #     # Set the piece at the given position
    #     game.set_piece(pos, piece)
    #
    #     # Check if the piece is placed at the correct position
    #     self.assertEqual(game.board[pos.row][pos.col], piece)
    #
    def test_capture(self):
        black_piece = GamePiece(PlayerColors.BLACK)
        white_piece = GamePiece(PlayerColors.WHITE)
        self.game.set_piece(Position(2, 2), black_piece)
        self.game.set_piece(Position(2, 3), white_piece)
        self.game.set_piece(Position(3, 2), black_piece)
        self.game.set_piece(Position(3, 3), white_piece)
        self.assertFalse(self.gp.capture_count, -1)

    def test_capture_single_piece(self):
        #White is surrounded by black
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 2), GamePiece(PlayerColors.BLACK))

        self.game.capture()
        self.assertIsNone(self.game.board[1][1])  #white is captured

    def test_no_capture(self):
        #white is placed with liberties
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))

        self.game.capture()
        self.assertIsNotNone(self.game.board[1][1])  #white not captured

    def test_capture_group(self):
        #White group surrounded by black
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(1, 2), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(0, 2), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 3), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 2), GamePiece(PlayerColors.BLACK))

        self.game.capture()
        self.assertIsNone(self.game.board[1][1])  #A group should be captured
        self.assertIsNone(self.game.board[1][2])

    def test_capture_count_single(self):
        #white is surrounded by black
        self.game.player1 = GamePlayer(PlayerColors.BLACK)
        self.game.player2 = GamePlayer(PlayerColors.WHITE)
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 2), GamePiece(PlayerColors.BLACK))
        initial_count = self.game.player1.capture_count
        self.game.capture()
        self.assertEqual(self.game.player1.capture_count, initial_count + 1) # 1 black should capture, might be too early to work

    def test_capture_count_group(self):
        #White group surrounded by black group
        self.game.player1 = GamePlayer(PlayerColors.BLACK)
        self.game.player2 = GamePlayer(PlayerColors.WHITE)
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(1, 2), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(0, 2), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 3), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(2, 2), GamePiece(PlayerColors.BLACK))

        initial_count = self.game.player1.capture_count
        self.game.capture()
        self.assertEqual(self.game.player1.capture_count, initial_count + 2)#should be 2, might not work

    def test_capture_count_no_capture(self):
        #White piece with liberties

        self.game.player1 = GamePlayer(PlayerColors.BLACK)
        self.game.player2 = GamePlayer(PlayerColors.WHITE)
        self.game.set_piece(Position(1, 1), GamePiece(PlayerColors.WHITE))
        self.game.set_piece(Position(0, 1), GamePiece(PlayerColors.BLACK))
        self.game.set_piece(Position(1, 0), GamePiece(PlayerColors.BLACK))

        initial_count = self.game.player1.capture_count
        self.game.capture()
        self.assertEqual(self.game.player1.capture_count, initial_count)  #No capture


if __name__ == '__main__':
    unittest.main()
