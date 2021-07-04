import logging

from gomoku import *
from gomoku.npboard import Board


def test_board():
    board = Board()
    assert len(board.valid_moves()) == SIZE * SIZE

    won = None
    for i in range(1, 30):
        board.random_move(X)
        won = board.random_move(O)

    logging.info(f'\n{board}')
    logging.info(won)


def test_win_horiz():
    board = Board()
    board.move(1, 1, X)
    board.move(2, 1, X)
    board.move(3, 1, X)
    board.move(4, 1, X)
    won = board.move(5, 1, X, debug=True)
    assert won == X


def test_win_vert():
    board = Board()
    board.move(1, 1, X)
    board.move(1, 2, X)
    board.move(1, 3, X)
    board.move(1, 4, X)
    won = board.move(1, 5, X)
    assert won == X


def test_win_diag():
    board = Board()
    board.move(5, 1, X)
    board.move(4, 2, X)
    board.move(3, 3, X)
    board.move(2, 4, X)
    won = board.move(1, 5, X)
    assert won == X


def test_win_diag2():
    board = Board()
    board.move(1, 1, X)
    board.move(2, 2, X)
    board.move(3, 3, X)
    board.move(4, 4, X)
    won = board.move(5, 5, X)
    assert won == X
