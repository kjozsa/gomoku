import numpy

from gomoku import SIZE
from gomoku.game import Game
from gomoku.onehot import onehot


def test_onehot_finished():
    game = Game()
    game.play()
    assert onehot(game.board.board).size == 3 * SIZE * SIZE


def test_onehot_empty():
    game = Game()
    assert onehot(game.board.board).size == 3 * SIZE * SIZE


def test_onehot_simple():
    a = numpy.full((3, 3), '').reshape(-1)
    encoded = onehot(a)
    print(encoded)
    assert encoded.size == 9 * 3
