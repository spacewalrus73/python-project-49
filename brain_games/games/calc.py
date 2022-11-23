from random import randint
from brain_games.games_modules import constants
from brain_games.games_modules import calc_module


def generating_calc():
    number_1 = randint(1, 25)
    number_2 = randint(1, 25)
    operand = constants.LIST_OF_OPERANDS[randint(0, 2)]
    expression = str(number_1) + operand + str(number_2)
    answer = str(calc_module.to_calc(number_1, operand, number_2))
    return expression, answer
