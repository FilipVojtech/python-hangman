from database import Database


def print_hangman(hang_level):
    hangman_data_versions = Database('hangman', 'versions').find_one({'level': str(hang_level)})

    print(hangman_data_versions['art'])
