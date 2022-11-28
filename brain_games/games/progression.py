from random import randint

NUMBER_OF_ROUNDS = 3
RULES = 'What number is missing in the progression?'


def generating_game():
    expression = generating_progression()
    hidden_index = randint(0, len(expression) - 1)
    answer = str(expression[hidden_index])
    expression[hidden_index] = '..'
    expression = ' '.join(map(str, expression))
    return expression, answer


def generating_progression():
    start = randint(1, 10)
    stop = randint(25, 30)
    step = randint(2, 4)
    var_list = list(range(start, stop, step))
    return var_list
