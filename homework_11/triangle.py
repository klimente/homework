"""
Calculate area of triangle by Heron's formula.
"""
from itertools import chain, permutations
from functools import reduce
from operator import mul, add, sub, eq
from sys import exit




class Triangle:
    """
    Class to represent object triangle.

    >>> Triangle.__name__
    'Triangle'
    >>> Triangle.apex_of_triangle
    ('A', 'B', 'C')
    """
    apex_of_triangle = 'A', 'B', 'C'

    def __init__(self, a, b, c):
        """
        Initializes instance of a triangle by coordinates of apex.

        :param a: coordinate of point (x,y).
        :type a: tuple.
        :param b: coordinate of point (x,y).
        :type b: tuple.
        :param c: coordinate of point (x,y).
        :type c: tuple.
        :raises: ValueError, TypeError
        >>> instance = Triangle((3.0, 0.0), (0.0, 4.0), (0.0, 0.0))
        >>> instance.point_a
        (3.0, 0.0)
        >>> instance = Triangle((1, 2), (2, (3,)), ('c', 5))
        Traceback (most recent call last):
        ValueError: Coordinate value must be number
        >>> instance = Triangle((1, 2, 3), (2, (3,)), ('c', 5))
        Traceback (most recent call last):
        TypeError: Coordinates must have only 2 values
        >>> instance = Triangle((1, 2), [2, 3], [3, 4])
        Traceback (most recent call last):
        TypeError: Coordinates must be in tuple
        >>> Triangle((7, 1), (1, 9), (1, 1)).len_ac
        6.0
        """
        if any([len(x) != 2 for x in (a, b, c)]):
            raise TypeError("Coordinates must have only 2 values")

        if not all([isinstance(x, tuple) for x in (a, b, c)]):
            raise TypeError("Coordinates must be in tuple")

        if not all([isinstance(x, (float, int)) for x in chain(a, b, c)]):
            raise ValueError('Coordinate value must be number')
        self.point_a = a
        self.point_b = b
        self.point_c = c
        self.len_ab = self._length_calculate((self.point_a, self.point_b))
        self.len_ac = self._length_calculate((self.point_a, self.point_c))
        self.len_bc = self._length_calculate((self.point_b, self.point_c))

        if not all([(add(x[0], x[1]) > x[2]) for x in permutations(self.sides, 3)]):
            print(f'Points {a,b,c} do not form a triangle')
            exit(1)


    def _length_calculate(self, points):
        """
        Private method that calculate length between two points.

        :param points: 2 points of triangle side.
        :type points: tuple.
        :return: float -- length of a triangle side.
        :raises: SystemExit

        >>> Triangle((7, 1), (1, 9), (1, 1))._length_calculate(((0.0, 0.0), (0.0, 5.)))
        5.0
        >>> Triangle((7, 1),(1, 9), (1, 1))._length_calculate(((0.0, 0.5), (0.0, 0.5)))
        Traceback (most recent call last):
        SystemExit: 1
        """
        if all(eq(*x) for x in zip(*points)):
            print(f'Cannot form triangle. Because coordinates {points} are the same')
            exit(1)
        return float((reduce(add, tuple(sub(*x)**2 for x in zip(*points))))**0.5)

    @property
    def points(self):
        """
        Property that return points of vertices of the triangle.

        :return: tuple -- points of vertices of the triangle.

        >>> Triangle((7, 1), (1, 9), (1, 1)).points
        ((7, 1), (1, 9), (1, 1))
        """
        return self.point_a, self.point_b, self.point_c

    @property
    def sides(self):
        """
        Property to get lengths of triangle sides.

        :return: tuple -- lengths of triangle sides

        >>> Triangle((7, 1), (1, 9), (1, 1)).sides
        (10.0, 6.0, 8.0)
        """
        return self.len_ab, self.len_ac, self.len_bc

    @property
    def semiperimeter(self):
        """
        Property to get half of perimetr of triangle.

        :return: float -- semiperimetr.

        >>> Triangle((7,1),(1,9),(1,1)).semiperimeter
        12.0
        """
        return (reduce(add, self.sides))/2

    def _multipliers(self):
        """
        Private method to calculate tuple multipliers for Heron's formula.

        :return: tuple --  multipliers.

        >>> Triangle((7,1),(1,9),(1,1))._multipliers()
        (12.0, 2.0, 6.0, 4.0)
        """
        return tuple((self.semiperimeter - i) for i in (0,) + self.sides)

    def area_by_heron(self):
        """
        Method to calculate area of triangle by Heron's formula.

        :return: float -- area of triangle.

        >>> Triangle((7,1),(1,9),(1,1)).area_by_heron()
        24.0
        """
        self._area = (reduce(mul, self._multipliers(), 1))**0.5
        return self._area


def parse_input(apex):
    """
    Function to get coordinates of points by parsing input.

    :param apex: name of point.
    :type apex: str.
    :return: tuple -- coordinate.
    :raises: SystemExit
    """
    x = input(f"Введите x для вершины {apex}: ")
    try:
        x = float(x)
    except ValueError:
        print(f"Cannot convert '{x}' to float. Coordinat value must be a number.")
        exit(1)
    y = input(f'Введите y для вершины {apex}: ')
    try:
        y = float(y)
    except ValueError:
        print(f"Cannot convert '{y}' to float. Coordinat value must be a number.")
        exit(1)
    return x, y


def tuple_points(func, iterable):
    """
    Function that make a tuple that computes the function
    using arguments from each of the iterables.

    :param func: some function that takes args from itarable.
    :type func: functrion
    :param iterable: iterable obj that need to modify.
    :return iterable: iterable object.

    >>> tuple_points(lambda x: str(x), [1, 2])
    ('1', '2')
    >>> tuple_points(lambda x: str(x), 3)
    Traceback (most recent call last):
    ValueError: Object 3 is not iterable
    >>> tuple_points(Triangle.__name__, [1, 2])
    Traceback (most recent call last):
    ValueError: Object Triangle is not callable
    """
    if not callable(func):
        raise ValueError(f'Object {func} is not callable')
    if not hasattr(iterable, '__iter__'):
        raise ValueError(f'Object {iterable} is not iterable')
    return tuple(map(func, iterable))

def show_program_name():
    """
    Function to display a name of purpose function main.

    :returns: None

    >>> show_program_name()
    Вычисление площади Герона по координатам.
    """
    print("Вычисление площади Герона по координатам.")

def main(parsing, apex):
    """
    Main function of the module.
    That calculates area of a triangle by input coordinates.

    :param parsing: function to get coordinate of point.
    :type parsing: function.
    :param apex: apex of a triangle or something.
    :return: str -- area of the triangle.
    """
    show_program_name()
    some_tr = Triangle(*tuple_points(parsing, apex))
    return f'Площадь треуголиника равна : {some_tr.area_by_heron()}'

if __name__ == '__main__':

    import doctest

    #Запустить тесты из текстового файла.
    #doctest.testfile('triangle.txt')

    #Запустить в тестовом режиме.
    #doctest.testmod()

    #Попробовать программу вручную.
    print(main(parse_input,Triangle.apex_of_triangle))
