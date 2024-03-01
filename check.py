from exceptions import OutOfRangeError, AlreadyChosenError


def player_answer(answer: str, answer_range: list):
    if answer.isnumeric():
        return is_player_answer_available(answer_number=int(answer), answer_range=answer_range)
    else:
        raise ValueError


def player_name(name: str):
    if name.isalpha():
        return name.capitalize()
    else:
        return 0


def is_player_answer_available(answer_number: int, answer_range: list):
    if answer_number in answer_range:
        return answer_number
    elif answer_number in range(answer_range[0], answer_range[-1] + 1):
        raise AlreadyChosenError
    else:
        raise OutOfRangeError

