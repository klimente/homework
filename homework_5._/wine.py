"""Catalogue '100 World Wines'"""
import datetime


class Wine:
    """Representation of wines catalogue.
    """
    def __init__(self, name, trademark, country, date_of_birth):
        """Create instance of Wine class.

        :param name: Name of Wine.
        :param name: str.
        :param trademark: Trademark of wine.
        :param trademark: str.
        :param country: Country of wine.
        :param country: str.
        :param date_of_birth: Date of birth for wine.
        :param date_of_birth: tuple of int.
        :returns: instance of class Wine.
        :raises: AssertionError,ValueError.
        """
        assert isinstance(name, str), "Name must be str"
        assert isinstance(trademark, str), "Trademark must be str"
        assert isinstance(country, str), "Country must be str"
        assert isinstance(date_of_birth, tuple), "Date of birth must be tuple of int"
        self.name = name.title()
        self.trademark = trademark
        self.country = country.title()
        self.date_of_birth = datetime.date(*date_of_birth)

    def maturing_time(self, today_date):
        """Calculates maturing time in days and return number of days.

        :param today_date: Date of today.
        :param today_date: tuple of int.
        :returns: int -- number of days.
        :raises: AssertionError,ValueError.
        """
        assert isinstance(today_date, tuple), "Date must be tuple of int"
        today = datetime.date(*today_date)
        res = today - self.date_of_birth
        return res.days

if __name__ == "__main__":
    some_wine = Wine("Some_wine", "Some_mark", "some_country", (2012, 10, 12))
    print(some_wine.name)
    print(some_wine.trademark)
    print(some_wine.country)
    print(some_wine.date_of_birth)
    print(f"Maturing time is {some_wine.maturing_time((2018, 4, 7))} days")
    print("Change name")
    some_wine.name = "Some_other_name"
    print(some_wine.name)
    new_wine = Wine("""
    So 
    many 
    strings
    in 
    name""", """
    And
    Here
    """, "Here_only_one", (2010, 10, 2))
    print(new_wine.name)
    print(new_wine.trademark)
