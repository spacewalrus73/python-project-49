from random import randint
from math import gcd
from brain_games.engine import main_actions


# Func append in lists correct answers and random numbers
def to_find_gcd():
    condition = 'Find the greatest common divisor of given numbers.'
    lst = []
    answers = []
    len_lists = 3
    index = 1

    while index <= len_lists:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        answers.append(str(gcd(number_1, number_2)))
        item = str(number_1) + ' ' + str(number_2)
        lst.append(item)
        index += 1

    return condition, lst, answers


# Func send data to func in module engine
def push():
    condition, lst, answers = to_find_gcd()
    main_actions(condition, lst, answers)
