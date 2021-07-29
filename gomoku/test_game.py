import logging
import timeit

import pytest
from keras.models import load_model

from gomoku.game import Game


def test_game():
    count = 1000
    game = Game()
    logging.debug(f"starting benchmark of {count} games")
    result = timeit.timeit(lambda: game.play(), number=count)
    logging.info(f"{count} games in {result} seconds")
    logging.info(game)
    assert result < 3.0  # secs


# @pytest.mark.skip(reason="too slow")
def test_random_vs_trained():
    count = 100
    model = load_model('../trained/test2.h5')
    game = Game()
    logging.info(f"benchmarking {count} games, random vs trained model..")
    result = timeit.timeit(lambda: game.play(model), number=count)
    logging.info(f"{count} games in {result} seconds")
    logging.info(game)


if __name__ == '__main__':
    test_game()
