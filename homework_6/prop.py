"""Prop"""


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


if __name__ == "__main__":
    s = Something(10)
    print(s.attr)
