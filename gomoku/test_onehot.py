from gomoku.game import Game
from gomoku.onehot import onehot


def test_onehot():
    game = Game()
    game.play()
    onehot(game.board.board)
