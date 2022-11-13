from prompt import string


# It is an engine of the games, which send questions,
# get answers and compare the results
def main_actions(condition, lst, answers):
    name = string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{condition}')
    for i, item in enumerate(lst):
        user_answer = string(f"Question: {item}\nYour answer: ")
        if user_answer.lower().strip() == answers[i]:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answers[i]}'."
                  f" \nLet's try again, {name}!")
            break
        if user_answer.lower().strip() == answers[i] and i == 2:
            print(f'Congratulations, {name}!')
