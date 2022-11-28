from prompt import string
from brain_games.cli import welcome_user


def engine(game_module):
    user_name = welcome_user()
    print(game_module.RULES)
    for i in range(game_module.NUMBER_OF_ROUNDS):
        expression, answer = game_module.generating_game()
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
