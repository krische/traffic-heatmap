def drange(minimum, maximum, step):
    value = minimum
    while value <= maximum:
        yield value
        value += step
