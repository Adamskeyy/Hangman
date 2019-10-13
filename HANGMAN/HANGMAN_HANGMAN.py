from HANGMAN.chances.CHANCES_HANGMAN import Chances
from HANGMAN.words_from_file import Words as RandomWord


class Hangman:
    def __init__(self):
        self.word_to_find = [letter for letter in RandomWord().get_word()]
        self.chances = Chances()
        self.word = ['_' for i in self.word_to_find]

    def get_chances(self):
        return self.chances.get_chances()

    def get_word_to_guess(self) -> str:
        return ' '.join(self.word)

    def guess_letter(self, letter: str) -> None:
        if letter not in self.word_to_find:
            self.chances.decrease_chances()
        self.append_letter(letter)

    def are_all_letters_found(self):
        return '_' not in self.word

    def append_letter(self, letter: str) -> None:
        istart = 0
        for i in range (0, self.word_to_find.count(letter)):
            index = self.word_to_find.index(letter, istart)
            self.word[index] = letter
            istart = index + 1

    def is_it_word_to_find(self, word) -> bool:
        return word == self.get_word_to_find()

    def get_word_to_find(self) -> str:
        return ''.join(self.word_to_find)