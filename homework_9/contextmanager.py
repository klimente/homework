"""Context manager"""

from time import time
from datetime import date


class Cmanager:
    """Custom context manager.
    """
    def __init__(self, filename):
        """A method to initializes instance.

        :param filename: name and type of the output file.
        :type filename: str.
        :raises: TypeError.
        :returns: initialized instance.
        """
        if not isinstance(filename, str):
            raise TypeError("filename must be str")
        self.filename = filename
        self._open_file = None
        self._start = 0
        self._finish = 0


    def __enter__(self):
        """A method to enter the context manager.

        :returns: instance of the Cmanager.
        """
        self._start = time()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """A method to exit the context manager.

        :param exc_type: Type of a error.
        :type exc_type: type.
        :param exc_val: Value of a error.
        :type exc_val: exception.
        :param exc_tb: Traceback for a error.
        :type exc_tb: traceback.
        :returns: bool -- pass or reraise a exception.
        """
        if exc_type is not None:
            self._open_file = open(self.filename, 'w')
            self._finish = time() - self._start
            self._open_file.write(f" Тип ошибки: {exc_type} \n" +
                                  f" Значение ошибки: {exc_val} \n " +
                                  f" Время работы программы: {self._finish}\n"
                                  f" Дата работы программы: {date.today()}\n")
            self._open_file.close()
            return False
        return True


if __name__ == '__main__':
    with Cmanager("somefile.txt"):
        for i in range(100000):
            print("s")
        raise AssertionError("Some exception")
