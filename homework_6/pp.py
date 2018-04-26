"""
dsa
"""


def sqrt(value):
    """ Calculate

    :param value: source value
    :type value: int
    :returns: float -- result of calculate

    >>>sqrt(-1)
    Traceback (most recent call last):
    ...
    ValueError: Positive value requi
    red
    """
    if value <= 0:
        raise ValueError('Positive value required')
    return value ** 0.5

if __name__ == '__main__':
    import doctest
    doctest.testmod()