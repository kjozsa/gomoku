import logging

from keras.models import load_model

from gomoku import *
from gomoku.npboard import Board


def test_predict():
    board = Board()
    board.move(0, 0, X)
    board.move(5, 3, O)

    model = load_model('../trained/test.h5')
    x, y = board.predict(model)
    logging.info(f"predicted best move: {x}, {y}")
