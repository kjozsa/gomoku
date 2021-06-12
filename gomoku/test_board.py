import logging

from gomoku import *
from gomoku.npboard import Board


def test_board():
    board = Board()
    assert len(board.valid_moves()) == 100

    for i in range(1, 30):
        board.random_move(X)
        board.random_move(O)

    logging.info(board)
    logging.info(board.check_win())
