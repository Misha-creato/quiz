import requests
import random


class Question:
    difficulty_points = {
        "easy": 100,
        "medium": 200,
        "hard": 300,
    }

    def __init__(self, category: str, difficulty: str):
        self.category = category
        self.difficulty = difficulty
        self.question_dict = None
        self.correct_answer = None
        self.points = None
        self.answers = None

    def get_question_for_player(self):
        params = {
            'categories': self.category,
            'difficulties': self.difficulty,
            'limit': 1
        }
        response = requests.get(
            url="https://the-trivia-api.com/v2/questions",
            params=params
        )
        for i in response.json():
            question = i
        self.question_dict = question

    def check_answer(self, player_answer: int):
        if self.answers[player_answer] == self.correct_answer:
            return self.points
        else:
            return 0

    def get_correct_answer(self):
        self.correct_answer = self.question_dict['correctAnswer']

    def set_points(self):
        self.points = Question.difficulty_points[self.difficulty]

    def get_answers_dict(self):
        answers_list = []
        answers_list.extend(self.question_dict['incorrectAnswers'])
        answers_list.append(self.question_dict['correctAnswer'])
        random.shuffle(answers_list)
        answers_dict = enumerate(answers_list, 1)
        self.answers = dict(answers_dict)

    def prepare_question(self):
        print('Please wait, your question is loading...')
        self.get_question_for_player()
        self.get_correct_answer()
        self.set_points()
        self.get_answers_dict()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.selected_category_and_difficulty = None

    def update_score(self, points: int):
        self.score += points

