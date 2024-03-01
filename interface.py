from prettytable import PrettyTable
from service import Player
import check
from exceptions import OutOfRangeError, AlreadyChosenError

available_players_quantity = list(range(1, 16))


def print_all_categories(question_categories: dict):
    table = PrettyTable(["Category number", "Category and difficulty"])
    for key, value in question_categories.items():
        table.add_row(row=[key, value], divider=True)
    print(table)


def greeting():
    print('Hello! Welcome to Quiz Game!')


def get_players_number():
    while True:
        number_of_players = input('Input number of players: ')
        try:
            return check.player_answer(answer=number_of_players, answer_range=available_players_quantity)
        except ValueError:
            print('Number of players must be integer')
        except OutOfRangeError:
            print('Number of players must be in range 1-30')


def get_questions_quantity(number_of_players: int):
    while True:
        question_quantity = input('Input question quantity: ')
        available_questions_quantity = list(range(number_of_players, 31))
        try:
            return check.player_answer(answer=question_quantity, answer_range=available_questions_quantity)
        except ValueError:
            print('Question quantity must be integer')
        except OutOfRangeError:
            print(f'Question quantity must be number from {available_questions_quantity[0]} '
                  f'to {available_questions_quantity[-1]}')


def get_game_settings():
    number_of_players = get_players_number()
    question_quantity = get_questions_quantity(number_of_players)
    return number_of_players, question_quantity


def get_player_name(player_number: int):
    while True:
        name = input(f'Input name for player {player_number}: ')
        player_name = check.player_name(name)
        if player_name:
            return check.player_name(name)
        else:
            print('*------------------------*---------------------------*')
            print('Invalid name, please try again')
            print('Name must consist of letters only')
            print('*------------------------*---------------------------*')


def get_player_answer(player: Player = None, answer_range: list = None):
    input_question = 'Input answer number: '
    if answer_range:
        input_question = f'Select category and difficulty for player \033[1m{player.name}\033[0m: '
    else:
        answer_range = list(range(1, 5))
    while True:
        player_answer = input(input_question)
        try:
            return check.player_answer(answer=player_answer, answer_range=answer_range)
        except ValueError:
            print('Answer must be integer')
        except OutOfRangeError:
            print(f'Answer must number from {answer_range[0]} to {answer_range[-1]}')
        except AlreadyChosenError:
            print('This number already been chosen. Please select available number')


def print_question(player: Player, question_dict: dict, answers: dict):
    print('******************************************************')
    print(f'Question for player \033[1m{player.name}\033[0m:')
    question_text = question_dict['question']['text']
    print('*----------------------------------------------------*')
    print(question_text)
    print('*----------------------------------------------------*')
    print('Answer options:')
    print('*----------------------------------------------------*')
    for k, v in answers.items():
        print(f'{k}. {v}')
    print('*----------------------------------------------------*')
    print('******************************************************')


def print_results(players: list):
    print('The questions are over')
    print('*** Results ***')
    table = PrettyTable(["Player", "Total score"])
    for player in players:
        table.add_row(row=[player.name, player.score], divider=True)
    print(table)


def print_statistics(question_quantity: int, players: list):
    print(f'Questions left: {question_quantity}')
    table = PrettyTable(["Player", "Current score"])
    for player in players:
        table.add_row(row=[player.name, player.score], divider=True)
    print(table)


def print_question_correction(answer_points: int, correct_answer: str):
    if answer_points:
        print('Correct answer!')
    else:
        print('Incorrect answer')
        print(f'Correct answer is "{correct_answer}"')

