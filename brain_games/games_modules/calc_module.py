def to_calc(number_1, operand, number_2):
    if operand == ' + ':
        result = number_1 + number_2
    elif operand == ' - ':
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    return result
