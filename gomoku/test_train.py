import numpy

from gomoku import *
from gomoku.npboard import Board
from gomoku.onehot import onehot


def test_train():
    board = Board()
    train_x = onehot(board.board.reshape(-1))
    print(train_x.shape)
    next = X

    while board.won is None:
        next = O if next == X else X
        board.random_move(next)
        train_x = numpy.vstack((train_x, onehot(board.board)))

    print(train_x.shape)
