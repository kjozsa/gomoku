import numpy as np
from keras.models import load_model
from tensorflow import keras
from tensorflow.keras import layers

from gomoku import *
from gomoku.npboard import Board

logger = logging.getLogger(__name__)


def create_train_data(model=None):
    board = Board()
    train_x, train_y = {}, {}

    while board.won is None:
        current = board.current
        if model is None or current == X:
            board.random_move()
        else:
            board.predict_move(model)
        (x, y) = board.last_move

        moved_board = Board.empty_board()
        moved_board[x, y] = 0
        moved_board = moved_board.reshape(-1)

        train_x[current] = board.onehot() if current not in train_x else np.vstack((train_x[current], board.onehot()))
        train_y[current] = moved_board if current not in train_y else np.vstack((train_y[current], moved_board))

    score = SIZE * SIZE - board.steps
    score_x = score if board.won == X else -score
    score_o = score if board.won == O else -score
    train_y[O] = np.where(train_y[O] == '0', score_o, train_y[O])
    train_y[X] = np.where(train_y[X] == '0', score_x, train_y[X])

    train_y[O] = np.where(train_y[O] == ' ', 0, train_y[O])
    train_y[X] = np.where(train_y[X] == ' ', 0, train_y[X])
    train_y[O] = train_y[O].astype(np.int32)
    train_y[X] = train_y[X].astype(np.int32)

    logger.debug(f"train_x shape {train_x[X].shape}, train_y shape {train_y[X].shape}")
    return train_x, train_y


def train(load_path, save_path, batch_size=50, sample_size=100, random=True):
    model = load_or_create_model(load_path)

    for batch in range(0, batch_size):
        train_x = None
        train_y = None
        for i in range(0, sample_size):
            try:
                x, y = create_train_data() if random else create_train_data(model)
                train_x = x[O] if train_x is None else np.vstack((train_x, x[O]))
                train_y = y[O] if train_y is None else np.vstack((train_y, y[O]))
                train_x = np.vstack((train_x, x[X]))
                train_y = np.vstack((train_y, y[X]))
            except IndexError:
                pass  # game did not finish, skip the sample

        logs = model.train_on_batch(train_x, train_y, return_dict=True, reset_metrics=False)
        logger.info(f"batch #{batch}: {logs}")
        model.save(save_path)


def load_or_create_model(model_path):
    try:
        model = load_model(model_path)
        logger.info(f"pre-trained model loaded from {model_path}")
    except OSError:
        model = create_model()
        logger.info("starting with new model")
    return model


def create_model():
    model = keras.Sequential([
        layers.Dense(303, activation="relu"),
        layers.Dense(303, activation="relu"),
        layers.Dense(150, activation="relu"),
        layers.Dense(150, activation="relu"),
        layers.Dense(100, activation="tanh"),
    ])
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model
