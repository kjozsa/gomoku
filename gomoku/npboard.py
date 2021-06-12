import logging
from random import choice

import numpy as np

from gomoku import *


def rotate45(n, m, li):
    result = []
    ctr = 0
    while ctr < 2 * n - 1:
        result += ['.'] * abs(n - ctr - 1)
        lst = []

        for i in range(m):
            for j in range(n):
                if i + j == ctr:
                    lst.append(li[i][j])
        lst.reverse()
        result += [*lst]
        ctr += 1
    return result


def board_str(b):
    return '\n'.join([''.join(x) for x in b])


class Board:
    def __init__(self):
        self.board = np.full((10, 10), '.')

    def __str__(self):
        return board_str(self.board.tolist())

    def move(self, x, y, player):
        assert player in [O, X]
        self.board[x][y] = player

    def valid_moves(self):
        return np.argwhere(self.board == '.')

    def random_move(self, player):
        x, y = choice(self.valid_moves())
        self.move(x, y, player)

    def check_win(self):
        s = self.__str__()
        t = str(self.board.transpose())

        r1 = board_str(np.array(rotate45(10, 10, self.board)).reshape(19, -1))

        if X * 5 in s + t + r1:
            return X
        elif O * 5 in s + t + r1:
            return O
        else:
            return None
