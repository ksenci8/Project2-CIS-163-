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

class TestGoStep4(unittest.TestCase):
    def setUp(self):
        self.game = GoModel(6,6)

    def test_initial_board_size(self):
        self.assertEqual(len(self.game._GoModel__board), 6)

    def test_board_is_list(self):
        self.assertIsInstance(self.game._GoModel__board, list)

    def test_move_num_starts_at_one(self):
        self.assertEqual(self.game.move_num, 1)

    # def test_undo_raises_exception(self):
    #     with self.assertRaises(UndoException):
    #         self.game.undo()

    def test_copy_board_creates_new_list(self):
        copied_board = self.game.copy_board()
        self.assertIsInstance(copied_board, list)

    def setUp(self):
        self.model = GoModel()
        self.piece = GamePiece(PlayerColors.BLACK)

    def test_instance(self):
        self.assertIsInstance(self.model, GoModel)

    def test_add_piece(self):
        self.model.add_piece(self.piece, (3, 3))
        self.assertTrue((3, 3) in self.model.board)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            self.model.add_piece(self.piece, (-1, -1))  # Assuming negative positions are invalid

    def test_is_valid_placement_false(self):
        self.model.add_piece(self.piece, (3, 3))
        self.assertFalse(self.model.is_valid_placement(GamePiece("white"), (3, 3)))  # Position already occupied

    def test_is_valid_placement_true(self):
        self.assertTrue(self.model.is_valid_placement(self.piece, (4, 4)))  # Assuming empty positions are valid

    # def setUp(self):
    #     game = GoModel(6, 6)
    #
    # def test_initial_board_size(self):
    #     game = GoModel(6, 6)
    #     self.assertEqual(len(self.game._GoModel__board), 6)
    #
    # def test_board_is_list(self):
    #     game = GoModel(6, 6)
    #     self.assertIsInstance(self.game._GoModel__board, list)
    #
    # def test_move_num_starts_at_one(self):
    #     self.assertEqual(self.game.move_num, 1)
    #
    # def test_undo_raises_exception(self):
    #     with self.assertRaises(UndoException):
    #         self.game.undo()
    #
    # def test_copy_board_creates_new_list(self):
    #     copied_board = self.game.copy_board()
    #     self.assertIsInstance(copied_board, list)
    #
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
    # def test_capture(self):
    #     # Set up the GoModel with a 6x6 board
    #     game = GoModel(6, 6)
    #
    #     black_piece = GamePiece(PlayerColors.BLACK)
    #     white_piece = GamePiece(PlayerColors.WHITE)
    #
    #     game.set_piece(Position(2, 2), black_piece)  #black  at (2, 2)
    #     game.set_piece(Position(2, 3), white_piece)  #white piece at (2, 3)
    #     game.set_piece(Position(3, 2), black_piece)  #black piece at (3, 2)
    #     game.set_piece(Position(3, 3), white_piece)  #white piece at (3, 3)
    #
    #
    #     capture = game.capture()  #
    #
    #     print(capture)



if __name__ == '__main__':
    unittest.main()
