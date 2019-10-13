from HANGMAN.chances.CHANCES_ERROR_HANGMAN import ChancesError


class Chances:
    def __init__(self, chances=9):
        # self.chances = 9 if chances is None else chances
        self.chances = chances

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('Nie masz już szans :P')