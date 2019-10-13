from random import randint


class RandomWord:
    def __init__(self):
        self.HANGMAN = ('test', 'testtest')

    def get_word(self) -> str:
        index = randint(0, len(self.HANGMAN) - 1)
        return self.HANGMAN[index]