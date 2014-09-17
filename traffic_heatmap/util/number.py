def is_number(value):
    """
    Checks if a given input is a number
    :param value: Input string or number
    :return: True or False
    """
    try:
        float(value)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(value)
        return True
    except (TypeError, ValueError):
        pass

    return False


def drange(minimum, maximum, step):
    value = minimum
    while value <= maximum:
        yield value
        value += step
