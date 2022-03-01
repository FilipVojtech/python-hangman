import commands as cmd
from game import Game

if __name__ == '__main__':
    playing = False
    game: Game

    while True:
        choice = input('~> ')
        if choice == 'start':
            playing = True
            game = Game('')
        elif choice == 'load':
            game_code = input("Game code: ")
            try:
                game = Game(game_code)
            except TypeError as ignore:
                print('This game doesn\'t exist')
                continue
            playing = True

        elif choice == 'add':
            cmd.add()
        # elif choice == 'edit':
        #     cmd.edit()
        # elif choice == 'delete':
        #     cmd.delete()
        elif choice == 'help':
            cmd.help_command()
        elif choice == 'exit':
            exit()
        else:
            cmd.unknown()

        while playing:
            choice = input('#> ')
            if len(choice) == 1:
                # noinspection PyUnboundLocalVariable
                game.guess(choice)
            elif choice == 'save':
                cmd.save(game)
                playing = False
            elif choice == 'stop':
                playing = False
            # elif choice == 'word':
            #     game.show_word()
            elif choice == 'help':
                cmd.help_command()
            elif choice == 'exit':
                exit()
            else:
                cmd.unknown()

            if len(game.uhodnute) - len(set(game.word)) == 0:
                print('You won!')
                cmd.delete_game(game.game_code)
                playing = False
            elif len(game.guessed) - len(game.uhodnute) == 6:
                print('You lost!')
                print('The word was ' + game.word)
                cmd.delete_game(game.game_code)
                playing = False
