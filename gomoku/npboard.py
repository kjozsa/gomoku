import logging
from random import choice

import numpy as np

from gomoku import *


def rotate45(matrix):
    n = len(matrix)
    result = []
    ctr = 0
    while ctr < 2 * n - 1:
        result += ['.'] * abs(n - ctr - 1)
        lst = []

        for i in range(n):
            for j in range(n):
                if i + j == ctr:
                    lst.append(matrix[i][j])
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
        t = board_str(self.board.transpose().tolist())
        r1 = board_str(np.array(rotate45(self.board)).reshape(19, -1))
        r2 = board_str(np.array(rotate45(np.rot90(self.board))).reshape(19, -1))
        boards = s + t + r1 + r2

        if X * 5 in boards:
            return X
        elif O * 5 in boards:
            return O
        else:
            return None
