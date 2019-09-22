from unittest import TestCase

from Chessnut import fen


class TestFEN4(TestCase):
    default_fen = "R-0,0,0,0-1,1,1,1-1,1,1,1-0,0,0,0-0-3,yR,yN,yB,yK,yQ,yB,yN,yR,3/3,yP,yP,yP,yP,yP,yP,yP,yP,3/14/" + \
                  "bR,bP,10,gP,gR/bN,bP,10,gP,gN/bB,bP,10,gP,gB/bK,bP,10,gP,gQ/bQ,bP,10,gP,gK/bB,bP,10,gP,gB/bN,bP" + \
                  ",10,gP,gN/bR,bP,10,gP,gR/14/3,rP,rP,rP,rP,rP,rP,rP,rP,3/3,rR,rN,rB,rQ,rK,rB,rN,rR,3"

    def test_parse_fen(self):
        fen_parts = fen.FEN4.parse_fen(self.default_fen)
        self.assertEqual(7, len(fen_parts))
        eliminated_players = fen.FEN4.parse_fen_part(fen_parts[fen.FEN4.PART.ELIMINATED_PLAYERS.value])
        self.assertEqual(4, len(eliminated_players))
        raster = fen.FEN4.parse_fen_piece_placement(fen_parts[fen.FEN4.PART.PIECE_PLACEMENT.value])
        self.assertEqual(196, len(raster))
