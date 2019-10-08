"""
Generates and returns a dictionary containing the superset of (i.e., all)
legal moves on a four player chessboard.
"""

from math import atan2
from copy import deepcopy

row_size = 14
raster_size = row_size * row_size
DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1),  # straight lines
              (-1, 0), (-1, -1), (0, -1), (1, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1),  # knights
              (-2, -1), (-1, -2), (1, -2), (2, -1),
              ]
RAYS = [atan2(d[1], d[0]) for d in DIRECTIONS]

PIECES = {'rK': lambda x, y, dx, dy: abs(dx) <= 1 and abs(dy) <= 1,
          'rQ': lambda x, y, dx, dy: dx == 0 or dy == 0 or abs(dx) == abs(dy),
          'rN': lambda x, y, dx, dy: (abs(dx) >= 1 and
                                      abs(dy) >= 1 and
                                      abs(dx) + abs(dy) == 3),
          'rB': lambda x, y, dx, dy: abs(dx) == abs(dy),
          'rR': lambda x, y, dx, dy: dx == 0 or dy == 0,
          'rP': lambda x, y, dx, dy: (1 < y < 8 and abs(dx) <= 1 and dy == 1),
          'bP': lambda x, y, dx, dy: (0 < x < 7 and 3 < y < 12 and abs(dy) <= 1 and dx == 1),
          'yP': lambda x, y, dx, dy: (8 < y < 14 and abs(dx) <= 1 and dy == -1),
          'gP': lambda x, y, dx, dy: (6 < x < 13 and 3 < y < 12 and abs(dy) <= 1 and dx == -1),
          }

# 3x3 corners of 14x14 board are excluded from game
EXCLUDED_IDX = {0, 1, 2, 11, 12, 13,
                14, 15, 16, 25, 26, 27,
                28, 29, 30, 39, 40, 41,
                154, 155, 156, 165, 166, 167,
                168, 169, 170, 179, 180, 181,
                182, 183, 184, 193, 194, 195}


def ij_to_dxdy(start_idx, end_idx, _row_size=14):
    """
    Helper function to calculate _x, _y, _dx, _dy given two indexes from the board
    Determine the row, change in column, and change in row
    # of the start/end point pair
    :param start_idx: starting index
    :param end_idx: ending index
    :param _row_size
    :return: _x, _y, _dx, _dy
    """
    #  for move validation
    _x = start_idx % _row_size
    _y = _row_size - start_idx // _row_size
    _dx = (end_idx % _row_size) - (start_idx % _row_size)
    _dy = (_row_size - end_idx // _row_size) - _y
    return _x, _y, _dx, _dy


MOVES = dict()

for sym, is_legal in PIECES.items():

    MOVES[sym] = list()

    for idx in range(raster_size):

        # Initialize arrays for each of the 8 possible directions that a
        # piece could be moved; some of these will be empty and
        # removed later
        MOVES[sym].append([list() for _ in range(8)])

        # Sorting the list of end points by distance from the starting
        # point ensures that the ouptut order is properly sorted
        for end in sorted(range(raster_size), key=lambda x: abs(x - idx)):
            x, y, dx, dy = ij_to_dxdy(idx, end)

            if idx == end or idx in EXCLUDED_IDX or end in EXCLUDED_IDX or not is_legal(x, y, dx, dy):
                continue

            angle = atan2(dy, dx)
            if angle in RAYS:
                # Mod by 8 to shift the ray index of knight moves down
                # by 8 from the index found in DIRECTIONS; the ray index of
                # all other pieces will be unchanged
                ray_num = RAYS.index(angle) % 8
                MOVES[sym][idx][ray_num].append(end)

        # Remove unused (empty) lists
        MOVES[sym][idx] = [r for r in MOVES[sym][idx] if r]

for sym in ['K', 'Q', 'N', 'B', 'R']:
    for color in ['b', 'y', 'g']:
        MOVES[color + sym] = deepcopy(MOVES['r' + sym])

# Directly add castling for kings
MOVES['rK'][189][0].append(189 + 2)
MOVES['rK'][189][4].append(189 - 2)
MOVES['bK'][84][2].append(56)
MOVES['bK'][84][3].append(112)
MOVES['yK'][6][0].append(8)
MOVES['yK'][6][1].append(4)
MOVES['gK'][111][0].append(83)
MOVES['gK'][111][4].append(139)

# Directly add double-space pawn opening moves
for i in range(8):
    MOVES['rP'][171 + i][0 if i == 7 else 1].append(143 + i)
    MOVES['bP'][43 + 14 * i][0].append(45 + 14 * i)
    MOVES['yP'][17 + i][0 if i == 0 else 1].append(45 + i)
    MOVES['gP'][54 + 14 * i][0 if i == 0 else 1].append(52 + 14 * i)
