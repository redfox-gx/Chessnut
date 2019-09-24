"""

https://en.wikibooks.org/wiki/Four-Player_Chess/Notation
"""
from enum import Enum, unique


class FEN4:
    """
    FEN4 https://en.wikibooks.org/wiki/Four-Player_Chess/Notation
    """
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
                if piece.isnumeric():
                    space_count = int(piece)
                    pieces_raster.extend([' '] * space_count)
                else:
                    pieces_raster.extend([piece])
        return pieces_raster

    @staticmethod
    def generate_fen_piece_placement(piece_raster:list, row_size:int):
        pos = []
        for idx, piece in enumerate(piece_raster):
            if idx > 0 and idx % row_size == 0:
                # end of row line separator and append count
                pos.extend('/')
            if str(piece).isspace():
                if pos and pos[-1].isnumeric():
                    pos[-1] = str(int(pos[-1]) + 1)
                else:
                    pos.append('1')
            else:
                if pos and pos[-1].isnumeric():
                    pos.append(',')
                pos.append(piece)
                if idx % row_size != row_size - 1:
                    pos.append(',')
        return ''.join(pos)

