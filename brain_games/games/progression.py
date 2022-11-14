from random import randint
from brain_games.engine import main_actions


# Func makes progressions, replace 1 symbol in it to . .,
# and append this number to answers.
def making_progression():
    condition = 'What number is missing in the progression?'
    lst = []
    answers = []
    LEN_LISTS = 3
    index = 0
    while index < LEN_LISTS:
        start = randint(1, 10)
        stop = randint(25, 30)
        step = randint(2, 4)
        var_list = list(range(start, stop, step))
        hidden_index = randint(0, len(var_list) - 1)
        hidden_num = str(var_list[hidden_index])
        var_list[hidden_index] = '..'
        var_list = ' '.join(map(str, var_list))
        lst.append(var_list)
        answers.append(hidden_num)
        index += 1

    return condition, lst, answers


# Func send data to func in module engine
def push():
    condition, lst, answers = making_progression()
    main_actions(condition, lst, answers)
