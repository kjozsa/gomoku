import logging
from random import choice

import numpy as np

from gomoku import *


class Board:
    def __init__(self):
        self.board = np.full((10, 10), '.')

    def move(self, x, y, player, debug=False):
        assert player in [O, X]
        self.board[x][y] = player
        return self.check_win(x, y, debug)

    def valid_moves(self):
        return np.argwhere(self.board == '.')

    def random_move(self, player, debug=False):
        x, y = choice(self.valid_moves())
        return self.move(x, y, player, debug)

    def check_win(self, y, x, debug=False):
        row = self.board[y, 0:10]
        column = self.board[0:10, x]
        diagonal1 = self.board.diagonal(x - y)
        diagonal2 = np.rot90(self.board).diagonal(x - 9 + y)
        all = [''.join(x) for x in [row, column, diagonal1, diagonal2]]

        if debug:
            logging.debug(f"row: {row}")
            logging.debug(f"column: {column}")
            logging.debug(f"diagonal1: {diagonal1}")
            logging.debug(f"diagonal2: {diagonal2}")
            logging.debug(f"all: {all}")

        if any(X * 5 in z for z in all):
            return X
        elif any(O * 5 in z for z in all):
            return O
        else:
            return None
