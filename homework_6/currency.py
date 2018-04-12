"""Currency"""

import abc
import functools
import decimal


class Course:
    """Data descriptor to attribute course.
    """
    def __init__(self):
        """Data about courses in descriptor.
        """
        self.data = {('Euro', 'Dollar'):decimal.Decimal('1.23'),
                     ('Dollar', 'Euro'): decimal.Decimal('0.81'),
                     ('Rubble', 'Euro'): decimal.Decimal('0.012'),
                     ('Rubble', 'Dollar'): decimal.Decimal('0.015'),
                     ('Dollar', 'Rubble'): decimal.Decimal('64'),
                     ('Euro', 'Rubble'): decimal.Decimal('79'),
                     ('Euro', 'Euro'): decimal.Decimal(1),
                     ('Rubble', 'Rubble'): decimal.Decimal(1),
                     ('Dollar', 'Dollar'): decimal.Decimal(1)
                    }


    def __get__(self, instance, owner):
        """A method to get value for key from data.

        :returns function -- inner function that get value.
        """
        def inner(currenc):
            """A function to get argument from attribute.

            :param currenc: Class of Currency inheritors.
            :param currenc: Class.
            :returns: decimal -- value of courses.
            :raises: AttributeError.
            """

            if (owner.__name__, currenc.__name__) not in self.data:
                raise AttributeError
            #возвращаю значение по имени "владеющего" класса
            return self.data[(owner.__name__, currenc.__name__)]
        return inner


    def __set__(self, instance, value):
        """A method to set value in data of courses.
        """
        self.data[(instance.__class__.__name__, value[1].__name__)] = decimal.Decimal(value[0])
        self.data[(value[1].__name__,instance.__class__.__name__)] = decimal.Decimal('1')/decimal.Decimal(value[0])


class Currency(metaclass=abc.ABCMeta):
    """Abstract class to provide interface to inheritors.
    """
    course = Course()


    def __init__(self, value):
        """Creating instance of any inheritors class.

        :param value: value of currrency.
        :param value: int.
        :returns: instance of currency.
        :raises: TypeError."""
        if value < 0:
            raise TypeError("Value must be positive.")
        self.value = decimal.Decimal(value)


    @abc.abstractmethod
    def __str__(self):
        """Representation of currency.
        """
        pass


    def to(self, cls):
        """A method to convert inheritance of currency.

        :param cls: class of converted currency.
        :param cls: cls.
        :returns: instance -- of cls currency"""
        return cls(self.value * self.course(cls))


    @abc.abstractmethod
    def __add__(self, other):
        """A method to provide ability to addiction.

        :param other: other currency inheritor.
        :param other: Currency.
        """
        pass


    @abc.abstractmethod
    def __sub__(self, other):
        """A method to provide ability to subtract.

        :param other: other currency inheritor.
        :param other: Currency.
        """
        pass


    @abc.abstractmethod
    def __eq__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        """
        pass


    @abc.abstractmethod
    def __lt__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        """
        pass


    def __radd__(self, other):
        """A method to provide ability to add currency to zero for 'sum'.
        """
        if other == 0:
            return self
        else:
            raise TypeError("unsopperted operand")


@functools.total_ordering
class Euro(Currency):
    """Class to represent currency - Euro.
    """
    def __str__(self):
        """Represent Euro.

        :returns: str -- strin representation.
        """
        return f"{self.value} €"


    def __sub__(self, other):
        """A method to provide ability to subtract.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: instance of Euro.
        """
        return Euro(self.value - other.to(self.__class__).value)


    def __add__(self, other):
        """A method to provide ability to addiction.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns instance of Euro.
        """
        return Euro(self.value + other.to(self.__class__).value)


    def __eq__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: bool
        """
        return self.value == other.to(self.__class__).value


    def __lt__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: bool
        """
        return self.value < other.to(self.__class__).value


@functools.total_ordering
class Dollar(Currency):
    """Class to represent currency - Dollar.
    """

    def __str__(self):
        """Represent Dollar.

        :returns: str -- string representation.
        """
        return f"{self.value} $"


    def __sub__(self, other):
        """A method to provide ability to subtract.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: instance of Dollar.
        """
        return Dollar(self.value - other.to(self.__class__).value)


    def __add__(self, other):
        """A method to provide ability to addiction.

        :param other: other currency inheritor.
        :param other: Currency.
        :param other: instance of Dollar.
        """
        return Dollar(self.value + other.to(self.__class__).value)


    def __eq__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: bool
        """
        return self.value == other.to(self.__class__).value


    def __lt__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: bool
        """
        return self.value < other.to(self.__class__).value


@functools.total_ordering
class Rubble(Currency):
    """Class to represent currency - Rubble.
    """

    def __str__(self):
        """Represent Rubble.

        :returns: str -- string representation.
        """
        return f"{self.value} ₽"


    def __sub__(self, other):
        """A method to provide ability to subtract.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: instance of Rubble.
        """
        return Rubble(self.value - other.to(self.__class__).value)


    def __add__(self, other):
        """A method to provide ability to addiction.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: instance of Rubble.
        """
        return Rubble(self.value + other.to(self.__class__).value)


    def __eq__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns bool.
        """
        return self.value == other.to(self.__class__).value


    def __lt__(self, other):
        """A method to provide ability to compare currency.

        :param other: other currency inheritor.
        :param other: Currency.
        :returns: bool.
        """
        return self.value < other.to(self.__class__).value


    @staticmethod
    def impose_sanctions():
        """A method to simulate sanctions.

        :returns None.
        """
        Euro(1).course = (Euro.course(Rubble) * decimal.Decimal('1.5')), Rubble
        Dollar(1).course = (Dollar.course(Rubble) * decimal.Decimal('1.5')), Rubble



if __name__ == "__main__":

    e = Euro(5)
    print(f"Конвертим 5 евро в доллары : {e.to(Dollar)}")
    print(f"Конвертим 5 евро в рубли : {e.to(Rubble)}")
    r = Rubble(100)
    print(f"Конвертим 100 рублей в доллары : {r.to(Dollar)}")
    print(f"Конвертим 100 рублей в доллары : {r.to(Euro)}")
    print(f"Скдажываем 5 евро и 4 доллара : {e + Dollar(4)}")
    print(f"Отнимаем из 5 евро 100 рублей :{e - Rubble(100)}")
    print(f"Равен ли 1 евро 1 евро : {Euro(1) == Euro(1)}")
    print(f"Больше ли 5 евро 2-х долларов : {e >= Dollar(2)}")
    print(f"Курс доллара к рублю :{Dollar(4).course(Rubble)}")

    print(f"Курс евро к рублю :{Euro.course(Rubble)}")
    print(f"Сумма последовательности из 10 долларов{sum([Dollar(i) for i in range(10)])}")

    r.impose_sanctions()
    print("Вводим санкции на рубль")
    print(f"Проверяем курс Евро к рублю {Euro.course(Rubble)}")
    print(f"Проверяем курс Доллара к рублю {Dollar.course(Rubble)}")

