from random import shuffle
from sympy.ntheory import isprime
from brain_games.engine import main_actions


def is_prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    lst = []
    answers = []
    numbers_list = list(range(2, 100))
    shuffle(numbers_list)
    for num in range(3):
        lst.append(numbers_list[num])
        if isprime(numbers_list[num]) is True:
            answers.append('yes')
        else:
            answers.append('no')
    return condition, lst, answers


def push():
    condition, lst, answers = is_prime()
    main_actions(condition, lst, answers)

push()