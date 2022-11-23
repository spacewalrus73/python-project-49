from prompt import string
from brain_games.cli import welcome_user
from brain_games.games_modules import constants
from brain_games.games import even, calc, gcd, progression, prime


def even_game():
    user_name = welcome_user()
    print(constants.EVEN)
    for i in range(constants.NUMBER_OF_ROUNDS):
        number, answer = even.generating_even()
        user_answer = string(f"Question: {number}\nYour answer: ")
        if user_answer.strip().lower() == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f" \nLet's try again, {user_name}!")
            break
        if user_answer.strip().lower() == answer and i == 2:
            print(f'Congratulations, {user_name}!')


def calc_game():
    user_name = welcome_user()
    print(constants.CALC)
    for i in range(constants.NUMBER_OF_ROUNDS):
        expression, answer = calc.generating_calc()
        user_answer = string(f"Question: {expression}\nYour answer: ")
        if user_answer.strip().lower() == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f" \nLet's try again, {user_name}!")
            break
        if user_answer.strip().lower() == answer and i == 2:
            print(f'Congratulations, {user_name}!')


def gcd_game():
    user_name = welcome_user()
    print(constants.GCD)
    for i in range(constants.NUMBER_OF_ROUNDS):
        expression, answer = gcd.to_find_gcd()
        user_answer = string(f"Question: {expression}\nYour answer: ")
        if user_answer.strip().lower() == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f" \nLet's try again, {user_name}!")
            break
        if user_answer.strip().lower() == answer and i == 2:
            print(f'Congratulations, {user_name}!')


def progression_game():
    user_name = welcome_user()
    print(constants.PROGRESSION)
    for i in range(constants.NUMBER_OF_ROUNDS):
        expression, answer = progression.setting_progression()
        user_answer = string(f"Question: {expression}\nYour answer: ")
        if user_answer.strip().lower() == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f" \nLet's try again, {user_name}!")
            break
        if user_answer.strip().lower() == answer and i == 2:
            print(f'Congratulations, {user_name}!')


def prime_game():
    user_name = welcome_user()
    print(constants.PRIME)
    for i in range(constants.NUMBER_OF_ROUNDS):
        number, answer = prime.generating_prime()
        user_answer = string(f"Question: {number}\nYour answer: ")
        if user_answer.strip().lower() == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f" \nLet's try again, {user_name}!")
            break
        if user_answer.strip().lower() == answer and i == 2:
            print(f'Congratulations, {user_name}!')
