

def check_player_answer(input_question: str, answer_range: list):
    while True:
        user_answer = input(input_question)
        if user_answer.isnumeric() and int(user_answer) in answer_range:
            return int(user_answer)
        elif user_answer.isnumeric() and int(user_answer) in range(1, answer_range[-1]+1):
            print('*------------------------*---------------------------*')
            print('This number already was selected. Please select available number')
            print('*------------------------*---------------------------*')
        else:
            print('*------------------------*---------------------------*')
            print('Invalid number, please try again')
            print(f'Answer must be number from {answer_range[0]} to {answer_range[-1]}')
            print('*------------------------*---------------------------*')


def check_player_name(player_number: int):
    while True:
        name = input(f'Input name for player {player_number}: ')
        if name.isalpha():
            return name.capitalize()
        else:
            print('*------------------------*---------------------------*')
            print('Invalid name, please try again')
            print('Name must consist of letters only')
            print('*------------------------*---------------------------*')


def check_game_settings():
    while True:
        number_of_players = input('Input number of players: ')
        players = check_player_answer(number_of_players, answer_range=list(range(1, 31)))
        question_quantity = input('Input question quantity: ')
        questions = check_player_answer(question_quantity, answer_range=list(range(1, 31)))
        if not players > questions:
            print('Question quantity must be greater than number of players!')
        else:
            return players, questions