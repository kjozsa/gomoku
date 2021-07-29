import logging

from keras.models import load_model

from gomoku import *
from gomoku.npboard import Board


def test_play():
    board = Board()
    board.move(0, 0, X)
    board.move(5, 3, O)

    model = load_model('../trained/gomoku2.h5')
    p = board.predict(model)
    logging.info(p)
