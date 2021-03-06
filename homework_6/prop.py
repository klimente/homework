#!/usr/bin/env python3.6

"""Prop"""
"""
    Дескриптор - класс который в методе инит может принять функцию 
    и с помощью протоколов меняет поведения переданного атрибута(на выдачу результата(из класса и объекта класса)
     удаление и изменение(только из объекта))
    Декоратор - функция которая что то принимает и модифицирует поведение функции или класса.
    (Предположение: что дескриптор работает изнутри , а декоратор как оболочка )
"""

class prop:
    """Descriptor that simulate property.
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        """Create instance of prop.

        :param fget: function to get value.
        :param fget: method
        :param fset: function to set value.
        :param fset: method.
        :param fdel: function to delete value.
        :param doc: documentation
        :param doc: str.
        :returns: prop.
        :raises: TypeError.
        """
        if fget is not None and not callable(fget):
            raise TypeError("fget must be method")
        if fset is not None and not callable(fset):
            raise TypeError("fset must be method")
        if fdel is not None and not callable(fset):
            raise TypeError("fdel must be method")
        if doc is not None and not isinstance(doc, str):
            raise TypeError("doc must be string")
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner=None):
        """A method to convert method to attribute get.

        :returns: some_value.
        :raises: AttributeError.
        """
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        """A method to convert method to attribute set.

        :returns: None.
        :raises: AttributeError.
        """
        if self.fset is None:
            raise AttributeError("can't get attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        """A method to convert method to attribute del.

        :returns: None.
        :raises: AttributeError.
        """
        if self.fdel is None:
            raise AttributeError("can't get attribute")
        self.fdel(instance)

    def getter(self, fget):
        """ A method to make getter
        :param fget: property getter
        :param fget: function
        :returns: None
        """
        self.fget = fget

    def setter(self, fset):
        """ A method to make setter
        :param fset: property setter
        :param fset: function
        :returns: None
        """
        self.fset = fset

    def deleter(self, fdel):
        """ A method to make deleter
        :param fdel: property deleter
        :param fdel: function
        :returns: None
        """
        self.fdel = fdel

class Something:
    """Some class.
    """
    def __init__(self, x):
        """Some function.
        """
        self.x = x


    @prop
    def attr(self):
        """some method that use prop descriptor.
        """
        return self.x **2

    @attr.setter
    def attr_set(self,value):
        self.x = value

if __name__ == "__main__":
    s = Something(10)
    print(s.attr)
    s.attr = 12
    print(s.attr)