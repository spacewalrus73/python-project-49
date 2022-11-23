from random import randint
from brain_games.games_modules import even_module


def generating_even():
    number = randint(1, 50)
    if even_module.is_even(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
