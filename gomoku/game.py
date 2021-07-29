from gomoku.npboard import *

logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        self.score = {X: 0, O: 0}
        self.board = Board()

    def __repr__(self):
        return f"{self.score[X] + self.score[O]} games: {self.score}"

    def play(self, model=None):
        self.board = Board()
        try:
            while self.board.won is None:
                if model is None or self.board.current == X:
                    self.board.random_move()
                else:
                    self.board.predict_move(model)

            self.score[self.board.won] += 1
        except IndexError:
            logger.warning(f"Noone could win this game: \n{self.board}")
