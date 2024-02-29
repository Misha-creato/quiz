from interface import Game
from check import check_game_settings


def main():
    print('Hello')
    number_of_players, question_quantity = check_game_settings()
    game = Game(number_of_players=number_of_players, question_quantity=question_quantity)
    game.start_game()
