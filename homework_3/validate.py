"""Decorator validate"""
import functools


def validate(low_bounded=float('-inf'), upper_bound=float('inf')):
    """Decorator to validate function parameter and return decorated function or None.

    :params low_bounded: low bound for validating arguments.
    :params low_bounded: int.
    :params upper_bound: upper bound for validating arguments.
    :params upper_bound: int.
    :returns: function -- decorated function or None.
     """
    if isinstance(low_bounded, (int, float)) and isinstance(upper_bound, (int, float)):
        def decorator(func):
            """A function which get a decorated function

            :params func: decorated function
            :params func: function
            :returns: function
            """
            @functools.wraps(func)
            def inner(*args):
                """Internal function which get args of decorated function

                :params args: positional args of decorated function
                :params args: tuple
                :returns: function -- decorated function itself
                """
                valid = True
                #check that only one parametr have passed to avoid exception
                if len(args) == 1:
                    # check that object is iterable, isTuple and not None
                    if args[0].__iter__ and isinstance(args[0], tuple) and args[0]:
                        for i in args[0]:
                            # check boundaries, size and type (не уверен насчет типа)
                            if not isinstance(i, int) or upper_bound < i or len(args[0]) != 3 or i < low_bounded:
                                valid = False
                    else:
                        valid = False
                else:
                    valid = False
                return func(args[0]) if valid else print("Function call is not valid")
            return inner
        return decorator
    else:
        print("Boundaries is not correct")


@validate(low_bounded=0, upper_bound=256)
def set_pixel(pixel_values):
    """A function to create pixel.

    :param pixel_values: pixel
    :param pixel_values: tuple of int
    :returns: None
    """
    print("pixel created")


if __name__ == '__main__':

    #pixel created
    set_pixel((2, 10, 100))
    set_pixel((54, 32, 234))

    #finction call is not valid
    set_pixel({2, 10, 100})
    set_pixel([2, 10, 100])
    set_pixel((200, 2, 200), [1])
    set_pixel("123")
    set_pixel((1, 2, 3, 4))
    set_pixel((0, 300, 400))
    set_pixel(())
    set_pixel()

    print(set_pixel.__name__)
    print(set_pixel.__doc__)
