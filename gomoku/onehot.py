import logging

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from gomoku import X, O


def onehot(board):
    # logging.debug(f"board: \n{board}")
    board_linear = board.reshape(-1)
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(board_linear)
    # logging.debug(f"int encoded: \n{integer_encoded}")

    onehot_encoder = OneHotEncoder(sparse=False, categories=[[0, 1, 2]])
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)

    onehot_encoder.fit(integer_encoded)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded).reshape(-1)
    # logging.debug(f"onehot encoded:\n{onehot_encoded}")
    return onehot_encoded