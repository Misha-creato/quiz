from prettytable import PrettyTable
from service import Player, Question
from check import check_player_answer, check_player_name


class Game:
    categories = [
        "music",
        "sport_and_leisure",
        "film_and_tv",
        "arts_and_literature",
        "history",
        "society_and_culture",
        "science",
        "geography",
        "food_and_drink",
        "general_knowledge",
    ]
    difficulties = [
        "easy",
        "medium",
        "hard"
    ]
    is_player_right = True
    change_question = False

    def __init__(self, number_of_players: int, question_quantity: int):
        self.number_of_players = number_of_players
        self.quantity = question_quantity
        self.players = []
        self.question_categories = self.set_available_categories()

    def set_available_categories(self):
        question_categories = []
        for category in self.categories:
            for difficulty in self.difficulties:
                question_categories.append(f'{category}:{difficulty}')
        question_categories = dict(enumerate(question_categories, 1))
        return question_categories

    def create_players(self):
        for i in range(1, self.number_of_players + 1):
            name_for_player = check_player_name(player_number=i)
            player = Player(name_for_player)
            self.players.append(player)

    def print_all_categories(self):
        table = PrettyTable(["Category number", "Category and difficulty"])
        for key, value in self.question_categories.items():
            table.add_row(row=[key, value], divider=True)
        print(table)

    def create_questions(self):
        for player in self.players:
            self.change_question_for_player(player=player)

    def change_question_for_player(self, player: Player):
        self.print_all_categories()
        user_choice = check_player_answer(
            input_question=f'Select category and difficulty for player {player.name}: ',
            answer_range=list(self.question_categories.keys())
        )
        category_and_difficulty = self.question_categories.pop(user_choice)
        category, difficulty = category_and_difficulty.split(':')
        if player.selected_category_and_difficulty:
            player.selected_category_and_difficulty.category = category
            player.selected_category_and_difficulty.difficulty = difficulty
        else:
            player.selected_category_and_difficulty = Question(category, difficulty)

    def ask_question(self):
        for player in self.players:
            self.is_player_right = True
            if player.change_question:
                self.change_question_for_player(player)
            while self.is_player_right and self.quantity > 0:
                self.player_move(player=player)

    def print_results(self):
        print('*** Results ***')
        for player in self.players:
            print(f'Player {player.name} - {player.score} points')

    def player_move(self, player: Player):
        print(f'Question for player {player.name}:')
        player.selected_category_and_difficulty.prepare_question()
        player.selected_category_and_difficulty.print_question()
        player_answer = check_player_answer(
            input_question='Input answer number: ',
            answer_range=list(player.selected_category_and_difficulty.answers.keys())
        )
        answer_points = player.selected_category_and_difficulty.check_answer(player_answer)
        self.check_answer_points(player, answer_points)

    def check_answer_points(self, player: Player, answer_points: int):
        self.quantity -= 1
        if answer_points:
            print('Correct answer!')
            player.update_score(answer_points)
            self.change_question_for_player(player) if self.quantity else None
        else:
            self.is_player_right = False
            player.change_question = True
            print('Incorrect answer')

    def start_game(self):
        self.create_players()
        self.create_questions()
        while self.quantity:
            self.ask_question()
        self.print_results()

