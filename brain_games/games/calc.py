from random import randint


RULES = 'What is the result of the expression?'
LIST_OF_OPERANDS = [' + ', ' - ', ' * ']
NUMBER_OF_ROUNDS = 3


def generating_game():
    number_1 = randint(1, 25)
    number_2 = randint(1, 25)
    operand = LIST_OF_OPERANDS[randint(0, 2)]
    expression = str(number_1) + operand + str(number_2)
    answer = str(to_calc(number_1, operand, number_2))
    return expression, answer


def to_calc(number_1, operand, number_2):
    if operand == ' + ':
        result = number_1 + number_2
    elif operand == ' - ':
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    return result
