from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'
NUMBER_OF_ROUNDS = 3


def generating_game():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    expression = str(number_1) + ' ' + str(number_2)
    answer = str(gcd(number_1, number_2))
    return expression, answer
