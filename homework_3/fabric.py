"""Decorator maker"""

import functools

#INNER_DEC_ENABLED = True


# получаю lambada
def fabric(fabric_arg):
    """Decorator to decorate decorator and returns decorators as arg in lambda function or None.

    :param fabric_arg: lambda that wrapped input decorator (work with int operand).
    :param fabric_arg: function
    :returns: function -- function thar wrapped into fabric_arg lambda
    """

    INNER_DEC_ENABLED = True

    def off():
        nonlocal INNER_DEC_ENABLED
        INNER_DEC_ENABLED = False

    def on():
        nonlocal INNER_DEC_ENABLED
        INNER_DEC_ENABLED = True

    fabric.off = off
    fabric.on = on

    if callable(fabric_arg):

        # получаю декорируемы декоратор
        def decorator(dec):
            """Internal function that get decorator for decorating.

            :param dec: decorating decorator.
            :param dec: function.
            :returns: function.
            """
            # получаю аргументы декоратора
            @functools.wraps(dec)
            def decorator_arg(*dargs, **dkwargs):
                """Interna function that get arguments for input decorator.

                :param dargs: positional arguments for decorator
                :param dkwargs: named arguments for decorator
                :returns: function
                """
                # проверяю скобочки (наличие аргументов декоратора)
                if len(dargs) == 1 and not dkwargs and callable(dargs[0]):
                    @functools.wraps(dargs[0])
                    # получаю аргументы для ф-ции
                    def inner(*args, **kwargs):
                        """Internal arguments for internal function"""
                        # проверяю включиние декоратора (dec)
                        if INNER_DEC_ENABLED:
                            # ламбда(декор()(функция)(аргументы))
                            result = fabric_arg((dec()(dargs[0]))(*args, **kwargs))
                            print(result)
                            return result
                        # ламбда(функция(аргументы))
                        result = fabric_arg(dargs[0](*args, **kwargs))
                        print(result)
                        return result
                    return inner
                # если аргументы есть (или есть скобочки)
                else:
                    # получаю декорируму ф-цию
                    def decorated(func):
                        """Internal function"""
                        @functools.wraps(func)
                        def inner(*args, **kwargs):
                            """Internal arguments for internal function"""
                            # получаю аргументы для ф-ции
                            if INNER_DEC_ENABLED:
                                # ламбда(декор(аргументы декор)(функция)(аргументы))
                                result = fabric_arg((dec(*dargs)(func))(*args, **kwargs))
                                print(result)
                                return result
                            # ламбда(функция(аргументы))
                            result = fabric_arg(func(*args, **kwargs))
                            print(result)
                            return result
                        return inner
                    return decorated
            return decorator_arg
        return decorator
    else:
        print(f"{fabric_arg} - object is not callable")


# работает с числами
wrapper = lambda x: x**3


@fabric(wrapper)
def deco(some_arg=1):
    """Example of decorator that can be decorated with named argument

    :param some_arg: count of string "Working decorator" on screen
    :param some_arg: int
    :returns: function -- decorated function
    """
    def decorator(func):
        """Internal function"""
        def uppercase(*args, **kwargs):
            """Internal arguments for internal function"""
            for _ in range(some_arg):
                print("Working decorator")
            return func(*args, **kwargs)
        return uppercase
    return decorator

@deco(3)
def unfunny_mem(some_important_arg):
    """Example of function that returns int

    :param some_important_arg: just x
    :param some_important_arg: positional argument
    :returns: int -- only int
    """
    print("Working function that returns int")
    return 5


@deco
def funny_mem(some_important_arg):
    """Example of function that returns int

        :param some_important_arg: just x
        :param some_important_arg: positional argument
        :returns: int -- only int (for lambda)
        """
    print("Working function that returns int")
    return 10


if __name__ == '__main__':
    fabric.on()
    unfunny_mem([1, 2, 3])
    funny_mem("saasd")
    print(unfunny_mem.__name__)
    print(deco.__name__)

    print("-"*30)
    fabric.off()
    unfunny_mem([1, 2, 3])
    funny_mem("saasd")
    print(unfunny_mem.__name__)
    print(deco.__name__)
