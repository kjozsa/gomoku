import logging

import numpy as np
from keras.models import load_model
from tensorflow import keras
from tensorflow.keras import layers

from gomoku import *
from gomoku.npboard import Board
from gomoku.onehot import onehot

MODEL_PATH = '../trained/gomoku.h5'


def test_train_data():
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

    return train_x, train_y


def create_model():
    model = keras.Sequential([
        layers.Dense(300, activation="relu"),
        layers.Dense(300, activation="relu"),
        layers.Dense(150, activation="relu"),
        layers.Dense(150, activation="relu"),
        layers.Dense(100, activation="tanh"),
    ])
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def test_train():
    try:
        model = load_model(MODEL_PATH)
        logging.info(f"pre-trained model loaded from {MODEL_PATH}")
    except OSError:
        model = create_model()
        logging.info("starting with new model")

    for batch in range(1, 50):
        train_x = None
        train_y = None
        for i in range(1, 100):
            try:
                x, y = test_train_data()
                train_x = x[O] if train_x is None else np.vstack((train_x, x[O]))
                train_y = y[O] if train_y is None else np.vstack((train_y, y[O]))
                train_x = np.vstack((train_x, x[X]))
                train_y = np.vstack((train_y, y[X]))
            except IndexError:
                pass  # game did not finish, skip the sample

        logs = model.train_on_batch(train_x, train_y, return_dict=True, reset_metrics=False)
        logging.debug(f"batch #{batch}: {logs}")
        model.save(MODEL_PATH)
