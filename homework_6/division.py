"""Division in functional way"""


def get_count_pair():
    """A function to return number of pair.

    :returns: int -- count of pair.
    """
    return int(input("Введите количество пар: "))


def get_pair(count_pair):
    """A function to list of input pair.

    :param count_pair: number of pair in output list.
    :param count_pair: int.
    :returns: list of tuples.
    """
    return [tuple(input("Введите пару через пробел: ").split()) for _ in range(count_pair)]


def handler(pair):
    """A function to handle division of pair.

    :param pair: tuple of pair that need to divide.
    :param pair: tuple.
    :returns: None.
    """
    try:
        print(int(pair[0])/int(pair[1]))
    except ZeroDivisionError as ex:
        print(f"Error code :{ex}")
    except ValueError as ex:
        print(f"Error code: {ex}")
    except IndexError as ex:
        print(f"Error code:{ex}")

if __name__ == '__main__':
    list(map(handler, get_pair(get_count_pair())))
