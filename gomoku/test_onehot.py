import numpy

from gomoku import SIZE
from gomoku.game import Game
from gomoku.onehot import onehot


def test_onehot_finished():
    game = Game()
    game.play()
    assert game.board.onehot().size == 3 + SIZE * SIZE * 3


def test_onehot_empty():
    game = Game()
    assert game.board.onehot().size == 3 + SIZE * SIZE * 3


def test_onehot_simple():
    a = numpy.full((3, 3), '').reshape(-1)
    encoded = onehot(a)
    print(encoded)
    assert encoded.size == 9 * 3
