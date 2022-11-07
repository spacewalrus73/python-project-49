from brain_games.engine import main_actions
from random import shuffle, randint


# Func make lists of correct answers and random numbers, which need to calc
def to_calc():
    condition = 'What is the result of the expression?'
    lst = []
    answers = []
    numbers_list = []
    numbers_len = 6
    operands = [' + ', ' - ', ' * ']

    shuffle(operands)

    for i in range(numbers_len):
        numbers_list.append(randint(1, 100))

    counter_for_operands = 0

    for i, item in enumerate(numbers_list):
        if i % 2 == 0:
            first_char = str(item)
            if operands[counter_for_operands] == ' + ':
                answers.append(str(item + numbers_list[i + 1]))
            elif operands[counter_for_operands] == ' - ':
                answers.append(str(item - numbers_list[i + 1]))
            else:
                answers.append(str(item * numbers_list[i + 1]))
        else:
            lst.append(first_char + operands[counter_for_operands] + str(item))
            counter_for_operands += 1
    return condition, lst, answers


# Func send data to func in module engine
def push():
    condition, lst, answers = to_calc()
    main_actions(condition, lst, answers)
