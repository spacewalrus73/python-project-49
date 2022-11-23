from random import randint


def generating_progression():
    start = randint(1, 10)
    stop = randint(25, 30)
    step = randint(2, 4)
    var_list = list(range(start, stop, step))
    return var_list
