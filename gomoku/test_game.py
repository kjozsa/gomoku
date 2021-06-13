from gomoku.game import Game
import logging
import timeit


def test_game():
    count = 100
    game = Game()
    logging.debug(f"starting benchmark of {count} games")
    result = timeit.timeit(lambda: game.play(), number=count)
    logging.info(f"{count} games in {result} seconds")
    logging.info(game)
    assert result < 4.0  # secs


if __name__ == '__main__':
    test_game()
