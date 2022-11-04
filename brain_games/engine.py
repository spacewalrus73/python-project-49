from prompt import string

# It is an engine of the games, which send questions, get answers and compare the results
def main_actions(condition, lst, answers):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{condition}')
    for i, item in enumerate(lst):
        answ = string(f'Question: {item}\nYour answer: ')
        if answ.lower().strip() == answers[i]:
            print('Correct!')
        else:
            print(f"{answ} is wrong answer ;(."
                  f"Correct answer was {answers[i]}.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
