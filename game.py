from prettytable import PrettyTable
from service import Player, Question
import random
from interface import (get_player_name, get_player_answer, print_all_categories, print_question, print_results,
                       print_statistics, print_question_correction)


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
            name_for_player = get_player_name(player_number=i)
            player = Player(name_for_player)
            self.players.append(player)
        random.shuffle(self.players)

    def change_question_for_player(self, player: Player):
        print_all_categories(self.question_categories)
        user_choice = get_player_answer(
            player=player,
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
            while self.is_player_right and self.quantity > 0:
                print_statistics(question_quantity=self.quantity, players=self.players)
                self.change_question_for_player(player=player)
                player.selected_category_and_difficulty.prepare_question()
                self.player_move(player=player)

    def player_move(self, player: Player):
        print_question(
            player=player,
            question_dict=player.selected_category_and_difficulty.question_dict,
            answers=player.selected_category_and_difficulty.answers
        )
        player_answer = get_player_answer()
        answer_points = player.selected_category_and_difficulty.check_answer(player_answer)
        self.check_answer_points(player, answer_points)

    def check_answer_points(self, player: Player, answer_points: int):
        self.quantity -= 1
        print_question_correction(
            answer_points=answer_points,
            correct_answer=player.selected_category_and_difficulty.correct_answer
        )
        if answer_points:
            player.update_score(answer_points)
        else:
            self.is_player_right = False
            player.change_question = True

    def start_game(self):
        self.create_players()
        while self.quantity:
            self.ask_question()
        print_results(players=self.players)

