from brain_games.games_modules.prime_module import is_prime
from random import shuffle


def generating_prime():
    numbers_list = list(range(2, 101))
    shuffle(numbers_list)
    selected_number = numbers_list[0]
    answer = is_prime(selected_number)
    return selected_number, answer
