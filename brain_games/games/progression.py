from random import randint
from brain_games.games_modules.progression_module import generating_progression


def setting_progression():
    expression = generating_progression()
    hidden_index = randint(0, len(expression) - 1)
    answer = str(expression[hidden_index])
    expression[hidden_index] = '..'
    expression = ' '.join(map(str, expression))
    return expression, answer
