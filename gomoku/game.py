from gomoku.npboard import *


class Game:
    def __init__(self):
        self.score = {X: 0, O: 0}
        self.board = Board()
        self.next = X

    def __repr__(self):
        return f"{self.score[X] + self.score[O]} games: {self.score}"

    def play(self):
        try:
            won = None
            while won is None:
                won = self.board.random_move(self.next)
                self.next = O if self.next == X else X

            self.score[won] += 1
        except IndexError:
            logging.warning(f"Noone could win this game: \n{self.board}")
        self.board = Board()
