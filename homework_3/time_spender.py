"""Decorator to measure the execution times of dedicated function"""
import time
import functools


def time_spender(func):
    """A decorator that allows to measure the execution times of dedicated function.

    :param func: dedicated function.
    :param func: function.
    :returns: function -- wrapped function into this decorator.

    >>>@time_spender
    ...def some_func()
    ......

    >>>some_func()
    ...
    execution times - 0.0
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        """internal function that measure time and returns passed function with passed arguments.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        spent_time = finish_time - start_time
        print(f"execution times - {spent_time}")
        return result
    return inner


@time_spender
def some_very_short_func():
    """Some example function
    """
    for _ in range(1, 1000):
        print("hohohoho", end=" ")


def some_very_long_func():
    """Some example function
    """
    start_time = time.time()
    for _ in range(1, 1000):
        print("hohohoho", end=" ")
    finish_time = time.time()
    print(f"execution times - {finish_time - start_time}")


if __name__ == "__main__":
    some_very_short_func()
    some_very_long_func()
