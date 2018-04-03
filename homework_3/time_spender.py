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
    functools.wraps(func)

    def inner(*args, **kwargs):
        """internal function that measure time and returns passed function with passed arguments.
        """
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        spent_time = t2 - t1
        print(f"execution times - {spent_time}")
        return result
    return inner


@time_spender
def some_very_short_func():
    for i in range(1,1000):
        print("hohohoho",end=" ")


def some_very_long_func():
    t1 = time.time()
    for i in range(1,1000):
        print("hohohoho",end=" ")
    t2 = time.time()
    print(f"execution times - {t2-t1}")


if __name__ == "__main__":
    some_very_short_func()
    some_very_long_func()