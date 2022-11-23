def is_prime(selected_number):
    counter = 0
    for number in range(2, selected_number // 2 + 1):
        if selected_number % number == 0:
            counter += 1
            break
    if counter == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer
