from random import randint
import os

# wczytać zawartość pliku (może do listy? ;) )
# wylosować słowo z listy (albo innej takiej)
# zwrócić wylosowane słowo


# class Words:
#     words_list = [line for line in open('words_from_file/words.txt')]
#
#     def get_word(self) -> str:
#         index = randint(0, len(self.words_list) - 1)
#         return self.words_list[index]

class Words:
    def get_path(self): #ścieżka bezwzględna
        return os.path.abspath(os.path.dirname(__file__)) #zwraca bezwzględna ścieżkę words

    def get_word(self) -> str:
        lines = 0
        with open(f'{self.get_path()}/words.txt') as file:
            while file.readline():
                lines += 1

        random_line = randint(1, lines)

        word = None
        with open(f'{self.get_path()}/words.txt') as file:
            for i in range(0, random_line): #lub range(random_line)
                word = file.readline().strip() #strip wycina ostatni niedrukowalny znak

        return word

if __name__ == '__main__':
    word = Words()
    print(word.get_path())