from random import shuffle
from brain_games.engine import main_actions


def is_prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    lst = []
    answers = []
    numbers_list = list(range(2, 100))
    shuffle(numbers_list)
    len_lists = 3
    for num in range(len_lists):
        lst.append(numbers_list[num])
        counter = 0
        for i in range(2, numbers_list[num] // 2 + 1):
            if (numbers_list[num] % i == 0):
                counter += 1
        if (counter == 0):
            answers.append('yes')
        else:
            answers.append('no')
    return condition, lst, answers


def push():
    condition, lst, answers = is_prime()
    main_actions(condition, lst, answers)
