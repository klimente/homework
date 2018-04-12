"""LetterEater """
#прошу прощения, что без шебангов , не успел разобраться к следующей домащки разбирусь.

class Price:
    """Descriptor to handle attribute price.
    """

    def __get__(self, instance, owner):
        """A method to return value.

        :returns: value.
        """
        if instance is None:
            return self
        return instance.value


    def __set__(self, instance, value):
        """A method to handle value.

        :raises: ValueError.
        """
        if value > 100 or value < 0:
            raise ValueError("Price must be between 0 and 100.")
        instance.value = value


class Book:
    """Class that represent object book.
    """
    price = Price()


    def __init__(self, author, title, price):
        """Create instance of book.

        :param author: author of a book.
        :param author: str.
        :param title: title of a book.
        :param title: str.
        :param price: price of a book.
        :param price: int
        :returns: Book -- instance of a book.
        :raises: TypeError.
        """
        if not isinstance(author, str):
            raise TypeError("Author must be str")
        if not isinstance(title, str):
            raise TypeError("Title must be str")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a digit")
        self.author = author
        self.title = title.title()
        self.price = price


if __name__ == '__main__':
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    print(b.price)
    #raises exception
    #b.price = - 12
    #b.price = 101
