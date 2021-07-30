import logging

from keras.models import load_model

from gomoku import X
from gomoku.npboard import Board
from gomoku.trainer import load_or_create_model

logger = logging.getLogger(__name__)


def input_valid_move(board):
    x, y = None, None
    while not board.is_valid_move(x, y):
        try:
            if x is not None:
                logger.warning("invalid move, try again!")
            a, b = input(f'{board.current} moves to: ')
            x, y = ord(a) - 97, int(b)
        except ValueError:
            pass
    return x, y


def console_game():
    model = load_or_create_model('../trained/sqe-masked2.h5')
    board = Board()

    while board.won is None:
        if board.current == X:
            x, y = input_valid_move(board)
        else:
            x, y = board.predict(model)

        logger.debug(f"{board.current} making move to {x}, {y}")
        board.move(x, y)
        logger.debug(f"\n{board}")
    logger.info(f"GAME OVER, game lost by {board.current}")


if __name__ == '__main__':
    console_game()
