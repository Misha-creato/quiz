from game import Game
from interface import greeting, get_game_settings


def main():
    greeting()
    number_of_players, question_quantity = get_game_settings()
    game = Game(number_of_players=number_of_players, question_quantity=question_quantity)
    game.start_game()


if __name__ == '__main__':
    main()

