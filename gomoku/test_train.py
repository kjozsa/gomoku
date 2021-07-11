import logging

import numpy as np

from gomoku import *
from gomoku.npboard import Board
from gomoku.onehot import onehot


def test_train():
    board = Board()
    train_x = {}
    train_y = {}
    train_x[O] = onehot(board.board.reshape(-1))
    train_x[X] = onehot(board.board.reshape(-1))
    train_y[O] = None
    train_y[X] = None
    current = X

    while board.won is None:
        current = O if current == X else X
        board.random_move(current)
        (x, y) = board.last_move

        moved_board = Board.empty_board()
        moved_board[x, y] = 0
        moved_board = moved_board.reshape(-1)

        train_x[current] = np.vstack((train_x[current], onehot(board.board)))
        train_y[current] = moved_board if train_y[current] is None else np.vstack((train_y[current], moved_board))

    train_x[O] = np.delete(train_x[O], -1, axis=0)
    train_x[X] = np.delete(train_x[X], -1, axis=0)

    score = 100 - board.steps
    train_y[O] = np.where(train_y[O] == '0', score, train_y[O])
    train_y[X] = np.where(train_y[X] == '0', score, train_y[X])
    train_y[O] = np.where(train_y[O] == ' ', 0, train_y[O])
    train_y[X] = np.where(train_y[X] == ' ', 0, train_y[X])

    train_y[O] = train_y[O].astype(np.int32)
    train_y[X] = train_y[X].astype(np.int32)

    logging.debug(train_x[O].shape)
    logging.debug(train_y[O].shape)
    logging.debug(train_y[O])
    logging.debug(train_y[X])
