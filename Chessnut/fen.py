"""

https://en.wikibooks.org/wiki/Four-Player_Chess/Notation
"""
from enum import Enum, unique


class FEN4:
    @unique
    class PART(Enum):
        ACTIVE_PLAYER = 0
        ELIMINATED_PLAYERS = 1
        CASTLING_KINGS = 2
        CASTLING_QUEENS = 3
        POINTS = 4
        PLY_COUNT = 5
        PIECE_PLACEMENT = 6

    @staticmethod
    def parse_fen(fen4: str):
        fen4_parts = fen4.split('-')
        return fen4_parts

    @staticmethod
    def parse_fen_part(fen4_part: str):
        fen4_part_list = fen4_part.split(',')
        return fen4_part_list

    @staticmethod
    def parse_fen_piece_placement(fen4_pieces: str):
        fen4_pieces_rows = fen4_pieces.split('/')
        pieces_raster = []
        for row in fen4_pieces_rows:
            pieces = row.split(',')
            for piece in pieces:
                try:
                    space_count = int(piece)
                    pieces_raster.extend([' '] * space_count)
                    pass
                except ValueError:
                    pieces_raster.extend([piece])
        return pieces_raster
