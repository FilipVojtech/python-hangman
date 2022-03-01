from database import Database
from game import Game

words = Database('hangman', 'words')
gameDb = Database('hangman', 'games')


def save(game: Game):
    game_code = game.game_code
    _thing = gameDb.find_one({'gameCode': game_code})

    if not _thing:
        gameDb.insert({
            'gameCode': game.game_code,
            'word': game.word,
            'guessed': list(game.guessed),
        })
    else:
        gameDb.update({'gameCode': game_code}, {'$set': {'guessed': list(game.guessed)}})

    print('Game code: ' + game.game_code)


def add():
    word = ''
    words_arr: list = list()
    print('To stop adding words type "\\"')
    while word != '\\':
        word = input("Word: ")
        words_arr.append(word)
    words_arr.pop()
    words.add_words(words_arr)


def edit():  # maybe
    pass


def delete():
    pass


def help_command():
    print('(~) Menu commands:')
    print('  start   start a game')
    print('   load   load a saved game')
    print('    add   add words to the database')
    # print('   edit   edit a word in the database')  # maybe
    # print(' delete   delete a word from the database')
    print('   help   show help page')
    print('   exit   exit the app')
    print()
    print('(#) Game commands:')
    print(' [letter]   Write a single letter to guess')
    print('     save   save current status of the game')
    print('     stop   exit the game without saving')
    print('     help   show help page')
    print('     exit   exit the app without saving')


def unknown():
    print('Unknown command type "help" for list of commands')


def delete_game(game_code):
    gameDb.delete(game_code)
