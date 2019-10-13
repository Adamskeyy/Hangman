from HANGMAN.chances.CHANCES_ERROR_HANGMAN import ChancesError
from HANGMAN.HANGMAN_HANGMAN import Hangman


class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()

    def play(self):
        while True:
            print(f'Pozostała ilość szans: {self.hangman.get_chances()}')
            print(self.hangman.get_word_to_guess())
            letter = input('Podaj literę lub wyraz: ')

            if self.hangman.is_it_word_to_find(letter):
                self.win()
                break
            try:
                self.hangman.guess_letter(letter)
            except ChancesError: #przechwytuje wyjątek z chanceserror
                self.lose()
                break

            if self.hangman.are_all_letters_found():
                self.win()
                break

    def lose(self):
        print('\nSłabiaku!!!')
        self.print_word_to_find()

    def win(self):
        print('\nGratulacje!!!')
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'Szukane słowo to: {self.hangman.get_word_to_find()}')

def main_game():
    while True:
        game = HangmanGame()
        game.play()

        if input('Chcesz grać ponownie? [t/n]: ') == 'n':
            break

if __name__ == '__main__': #zabezpieczenie przed odpaleniem kodu w innym pliku od razu po imporcie, trzeba wywołać ręcznie za pomocą HangmanGame.maingame ???
    main_game()