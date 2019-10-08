
import unittest

from Chessnut.moves4p import MOVES


class MovesTest(unittest.TestCase):

    def test_rays_pawn(self):
        self.assertEqual([[158], [157, 143]], MOVES['rP'][171])
        self.assertEqual([[164, 150], [163]], MOVES['rP'][178])

        self.assertEqual([[44, 45], [58]], MOVES['bP'][43])
        self.assertEqual([[142, 143], [128]], MOVES['bP'][141])

        self.assertEqual([[31, 45], [32]], MOVES['yP'][17])
        self.assertEqual([[37], [38, 52]], MOVES['yP'][24])

        self.assertEqual([[137], [151, 150]], MOVES['gP'][152])
        self.assertEqual([[53, 52], [67]], MOVES['gP'][54])

    def test_moves(self):
        # test that all the pieces are in the dictionary
        for color in 'rbyg':
            for piece in 'KQBNRP':
                self.assertIn(color + piece, MOVES)

                # test that every starting position is in the dictionary
                for idx in range(196):
                    self.assertIsNotNone(MOVES[color + piece][idx])

                    # test ordering of moves in each ray (should radiate out
                    # from the starting index)
                    for ray in MOVES[color + piece][idx]:
                        sorted_ray = sorted(ray, key=lambda x: abs(x - idx))
                        self.assertEqual(ray, sorted_ray, 'idx: ' + str(idx))

        # verify that castling moves are present
        self.assertIn(191, MOVES['rK'][189][0])
        self.assertIn(187, MOVES['rK'][189][4])
        self.assertIn(56, MOVES['bK'][84][2])
        self.assertIn(112, MOVES['bK'][84][3])
        self.assertIn(8, MOVES['yK'][6][0])
        self.assertIn(4, MOVES['yK'][6][1])
        self.assertIn(83, MOVES['gK'][111][0])
        self.assertIn(139, MOVES['gK'][111][4])

