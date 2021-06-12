from random import choice
import logging

import numpy as np

from gomoku import *

def str(b):
    return '\n'.join([''.join(x) for x in b.tolist()])

class Board:
    def __init__(self):
        self.board = np.full((10, 10), '.')

    def __str__(self):
        return str(self.board)

    def move(self, x, y, player):
        assert player in [O, X]
        self.board[x][y] = player

    def valid_moves(self):
        return np.argwhere(self.board == '.')

    def random_move(self, player):
        x, y = choice(self.valid_moves())
        logging.debug(f"{player} to {x}, {y}")
        self.move(x, y, player)

    def check_win(self):
        s = self.__str__()
        t = str(self.board.transpose())
        if X * 5 in s + t:
            return X
        elif O * 5 in s + t:
            return O
        else:
            return None
