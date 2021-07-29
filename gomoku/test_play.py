import logging

from keras.models import load_model

from gomoku import *
from gomoku.npboard import Board


def test_play():
    board = Board()
    board.move(0, 0, X)
    board.move(5, 3, O)
    logging.info(board)
    logging.info(board.onehot())
    logging.info(board.onehot().shape)
    logging.info(board.onehot().reshape((300, 1)).shape)

    model = load_model('../trained/gomoku.h5')
    p = model.predict(board.onehot().reshape((1, 300)))
    logging.info(p)
