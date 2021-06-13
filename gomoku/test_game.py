import logging
import timeit

from gomoku.game import Game


def test_game():
    count = 1000
    game = Game()
    logging.debug(f"starting benchmark of {count} games")
    result = timeit.timeit(lambda: game.play(), number=count)
    logging.info(f"{count} games in {result} seconds")
    logging.info(game)
    assert result < 3.0  # secs


if __name__ == '__main__':
    test_game()
