from random import randint

import hangman_pictures as hang
from database import Database


def _generate_code():
    code = ''
    for _ in range(6):
        code += str(randint(1, 9))
    return code


class Game:
    game_code: str = None
    word: str = ''
    # _difficulty: int
    guessed: set
    uhodnute: set

    def __init__(self, game_code):
        if game_code == '':
            _object = Database('hangman', 'words').find_random()
            self.game_code = _generate_code()
            self.word = _object['word']
            self.guessed = set()
        else:
            _object = None
            _object = Database('hangman', 'games').find_one({'gameCode': game_code})
            self.game_code = _object['gameCode']
            self.word = _object['word']
            self.guessed = set(_object['guessed'])
        self.uhodnute = set(self.word) & self.guessed
        self._show_status(len(self.guessed) - len(self.uhodnute))
        self._letters()

    def guess(self, character):
        self.guessed.add(character)
        self.uhodnute = set(self.word) & self.guessed
        self._show_status(len(self.guessed) - len(self.uhodnute))
        self._letters()

    @staticmethod
    def _show_status(level):
        hang.print_hangman(level)

    def show_word(self):
        print(self.word)

    def _letters(self):
        napoveda = ''
        for letter in self.word:
            if letter in self.uhodnute:
                napoveda += letter + ' '
            else:
                napoveda += '_ '
        print(napoveda)
