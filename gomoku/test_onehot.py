from gomoku import SIZE
from gomoku.game import Game
from gomoku.onehot import onehot


def test_onehot():
    game = Game()
    game.play()
    assert onehot(game.board.board).size == 3 * SIZE * SIZE
