from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_OF_ROUNDS = 3


def generating_game():
    expression = randint(1, 50)
    if is_even(expression) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return expression, answer


def is_even(expression):
    if expression % 2 == 0:
        return True
    else:
        return False
