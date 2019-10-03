"""

https://en.wikibooks.org/wiki/Four-Player_Chess/Notation
"""
from enum import Enum, unique


class FEN:
    promotions = ['b', 'n', 'r', 'q']


class FEN4:
    """
    FEN4 https://en.wikibooks.org/wiki/Four-Player_Chess/Notation
    """
    default_fen_4p = "R-0,0,0,0-1,1,1,1-1,1,1,1-0,0,0,0-0-3,yR,yN,yB,yK,yQ,yB,yN,yR,3/3,yP,yP,yP,yP,yP,yP,yP,yP,3/14/" \
                     + \
                     "bR,bP,10,gP,gR/bN,bP,10,gP,gN/bB,bP,10,gP,gB/bK,bP,10,gP,gQ/bQ,bP,10,gP,gK/bB,bP,10,gP,gB/bN,bP" \
                     + \
                     ",10,gP,gN/bR,bP,10,gP,gR/14/3,rP,rP,rP,rP,rP,rP,rP,rP,3/3,rR,rN,rB,rQ,rK,rB,rN,rR,3"

    promotions = ['q']

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
    def generate_fen_game_state(state):
        """
        generates the first part of FEN4 format from State4P namedtuple
        :param state: State4P namedtuple
        :return: first part of FEN4 string
        """
        fen_game_state = ''
        for state_part in state:
            if type(state_part) is list:
                part = ','.join(str(x) for x in state_part)
                fen_game_state = '-'.join([fen_game_state, part])
            else:
                fen_game_state = str(state_part).upper()
        return fen_game_state

    @staticmethod
    def append_part(a, b):
        return '-'.join([a, b])

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

