import functools

def validate(low_bounded=float('-inf'), upper_bound=float('inf')):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            inner.passed = True
            for i in args[0]:
                if i > upper_bound or i < low_bounded:
                    inner.passed = False
            return func(*args, **kwargs) if inner.passed else print("Function call is not valid")#подсвеченное ис нот
        return inner
    return decorator


@validate(low_bounded=0,upper_bound=256)
def set_pixel(pixel_values):
    print("pixel created")

set_pixel((300, 2, 300))#вопрос про кол-во картежей
set_pixel((1, 2, 3))
print(set_pixel.__name__)


