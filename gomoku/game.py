from gomoku.npboard import *

logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        self.score = {X: 0, O: 0}
        self.board = Board()

    def __repr__(self):
        return f"{self.score[X] + self.score[O]} games: {self.score}"

    def play(self):
        self.board = Board()
        try:
            while self.board.won is None:
                self.board.random_move()

            self.score[self.board.won] += 1
        except IndexError:
            logger.warning(f"Noone could win this game: \n{self.board}")
