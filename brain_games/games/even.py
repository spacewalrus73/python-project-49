from random import randint
from brain_games.engine import main_actions


# Func make lists and append in it numbers and correct answers
def is_even():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    lst = []
    answers = []
    len_lists = 3
    for num in range(len_lists):
        lst.append(randint(1, 50))
        if lst[num] % 2 == 0:
            answers.append('yes')
        else:
            answers.append('no')
    return condition, lst, answers


# Func send data to func in module engine
def push():
    condition, lst, answers = is_even()
    main_actions(condition, lst, answers)
