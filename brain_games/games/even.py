from random import randint
from brain_games.engine import main_actions


# Func make lists and append in it numbers and correct answers
def is_even():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    lst = []
    answers = []
    for num in range(3):
        lst.append(randint(1, 50))
        if lst[num] % 2 == 0:
            answers.append('yes')
        else:
            answers.append('no')
    return condition, lst, answers

# Func send the data to func in module engine


def push():
    condition, lst, answers = is_even()
    main_actions(condition, lst, answers)

# Old code


'''def is_even():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numbers = []
    for number in range(3):
        numbers.append(randint(1, 20))
    answ, r_answ = '', ''
    i = 0
    while answ.lower().strip() == r_answ and i < 3:
        if numbers[i] % 2 == 0:
            r_answ = 'yes'
        else:
            r_answ = 'no'
        answ = string(f'Question: {numbers[i]} \nYour answer: ')
        if answ.lower().strip() == r_answ:
            print('Correct!')
            i += 1
        else:
            print(f"{answ} is wrong answer ;(. Correct answer was {r_answ}.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')'''
