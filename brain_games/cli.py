from prompt import string


def welcome_user():
    name = string('Welcome to the Brain Games!'
                  '\nMay I have your name? ')
    print(f'Hello, {name}!')
    return name
