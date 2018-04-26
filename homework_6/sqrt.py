"""
Squere root functions
"""

def sqrt(value):
    """ Calculate

    :param value: source value
    :type value: int
    :returns: float -- result of calculate
    """
    if value <= 0:
        raise ValueError('Positive value required')
    return value ** 0.5

def test_squere_of_9_positive():
    assert sqrt(9) == 3.0

def test_squere_of_9_non_positive():
    try:
        sqrt(-1)
    except ValueError as raised_exc:
        assert raised_exc.args[0] == 'Positive value required',\
            'Wrong exception text'
        return
    assert False, 'Exceeption did not'


if __name__ == '__main__':
    test_squere_of_9_non_positive()