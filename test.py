# testing for Project 2
import unittest
from game_piece import GamePiece
from player_colors import PlayerColors
from position import Position


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


if __name__ == '__main__':
    unittest.main()
