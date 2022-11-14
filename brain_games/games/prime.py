from random import shuffle
from brain_games.engine import main_actions


def is_prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    lst = []
    answers = []
    numbers_list = list(range(2, 100))
    LEN_LISTS = 3

    shuffle(numbers_list)

    for item in range(LEN_LISTS):
        selected_num = numbers_list[item]
        lst.append(selected_num)
        counter = 0
        for number in range(2, selected_num // 2 + 1):
            if (selected_num % number == 0):
                counter += 1
                break

        if counter == 0:
            answers.append('yes')
        else:
            answers.append('no')

    return condition, lst, answers


def push():
    condition, lst, answers = is_prime()
    main_actions(condition, lst, answers)
