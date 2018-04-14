import time
import contextlib

class MineManager(contextlib.ContextDecorator):
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def __enter__(self):
        self.t1 = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.time()-self.t1
        print(f"Код отработал {self.t2} секунд")
        return True

#magicmetod

@contextlib.contextmanager
def manager():
    t1 = time.time()
    yield
    t2 = time.time()-t1
    print(f"Код отработал {t2} секунд")


with MineManager():
    for i in range(10000):
        print("Hello",end=" ")


@MineManager()
def func():
    for i in range(10000):
        print("Hello",end=" ")

func()
