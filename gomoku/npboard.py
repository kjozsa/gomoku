import logging
from random import choice
from typing import Any

import numpy as np

from gomoku import *


class Board:
    last_move: tuple[Any, Any]

    def __init__(self):
        self.board = Board.empty_board()
        self.won = None
        self.steps = 0

    @staticmethod
    def empty_board():
        return np.full((SIZE, SIZE), EMPTY)

    def __str__(self):
        return '\n'.join([''.join(x) for x in self.board.tolist()])

    def move(self, x, y, player, debug=False):
        assert player in [O, X]
        assert self.board[x][y] == EMPTY
        self.board[x][y] = player
        self.steps += 1
        return self.check_win(x, y, debug)

    def valid_moves(self):
        return np.argwhere(self.board == EMPTY)

    def random_move(self, player, debug=False):
        x, y = choice(self.valid_moves())
        self.last_move = (x, y)
        return self.move(x, y, player, debug)

    def check_win(self, y, x, debug=False):
        row = self.board[y, 0:SIZE]
        column = self.board[0:SIZE, x]
        diagonal1 = self.board.diagonal(x - y)
        diagonal2 = np.rot90(self.board).diagonal(x - SIZE + 1 + y)
        all = [''.join(x) for x in [row, column, diagonal1, diagonal2]]

        if debug:
            logging.debug(f"row: {row}")
            logging.debug(f"column: {column}")
            logging.debug(f"diagonal1: {diagonal1}")
            logging.debug(f"diagonal2: {diagonal2}")
            logging.debug(f"all: {all}")

        if any(X * 5 in z for z in all):
            # logging.debug(f"won in {self.steps} steps")
            self.won = X
        elif any(O * 5 in z for z in all):
            # logging.debug(f"won in {self.steps} steps")
            self.won = O
        else:
            self.won = None

        return self.won
