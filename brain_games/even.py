from prompt import string
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


name = welcome_user()


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    global name
    numbers = []
    for number in range(3):
        numbers.append(randint(1, 20))
    answ, r_answ = '', ''
    i = 0
    while answ.lower() == r_answ and i < 3:
        if numbers[i] % 2 == 0:
            r_answ = 'yes'
        else:
            r_answ = 'no'
        answ = string(f'Question: {numbers[i]} \nAnswer: ')
        if answ.lower() == r_answ:
            print('Correct!')
            i += 1
        else:
            print(f"{answ} is wrong answer ;(. Correct answer was {r_answ}.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
