from gomoku.npboard import *

logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        self.score = {X: 0, O: 0}
        self.board = Board()

    def __repr__(self):
        return f"{self.score[X] + self.score[O]} games: {self.score}"

    def play(self, model_x=None, model_o=None):
        self.board = Board()
        try:
            while self.board.won is None:
                if (model_x is None and self.board.current == X) or (model_o is None and self.board.current == O):
                    self.board.random_move()
                else:
                    model = model_x if self.board.current == X else model_o
                    self.board.predict_move(model)

            self.score[self.board.won] += 1
        except IndexError:
            logger.warning(f"Noone could win this game: \n{self.board}")
