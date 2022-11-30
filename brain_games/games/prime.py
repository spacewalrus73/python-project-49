from random import shuffle


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generating_game():
    numbers_list = list(range(2, 101))
    shuffle(numbers_list)
    selected_number = numbers_list[0]
    if is_prime(selected_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return selected_number, answer


def is_prime(selected_number):
    counter = 0
    for number in range(2, selected_number // 2 + 1):
        if selected_number % number == 0:
            counter += 1
            break
    if counter == 0:
        return True
    else:
        return False
