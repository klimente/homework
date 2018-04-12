"""Vehicle"""

import abc


class Vehicle(metaclass=abc.ABCMeta):
    """Abstract class that represent some vehicle.
    """
    wheels = 0

    def __init__(self, model, date_of_birth, mileage, price):
        """Initial method to help inheritors to define vehicle.

         :param model: model of vehicle.
         :param model: str
         :param date_of_birth: data of release.
         :param date_of_birth: int.
         :param mileage: amount of distance in km.
         :param mileage: int.
         :param price: starting price.
         :param price: int.
         :returns: instance of vehicle.
         :raises: TypeError.
         """
        if not isinstance(model, str):
            raise TypeError("Model must be str")
        if not isinstance(date_of_birth, int) or date_of_birth < 0:
            raise TypeError("Date of bitrh of vehicle must be positive int")
        if not isinstance(mileage, int) or mileage < 0:
            raise TypeError("Mileage must be positive int")
        if not isinstance(price, (int, float)) or price < 0:
            raise TypeError("Price must be positive int")
        self.model = model
        self.date_of_birth = date_of_birth
        self.mileage = mileage
        self.price = price


    @abc.abstractmethod
    def vehicle_type(self):
        """Abstract method to define type of vehicle for inheritors.
        """
        pass


    @classmethod
    def is_motorcycle(cls):
        """Classmethod to define is that vehicle a motorcycle or not.

        :returns: bool -- is that motorcycle or what.
        :raises: AssertionError.
        """
        if cls.wheels > 3:
            return False
        elif cls.wheels == 2:
            return True
        else:
            raise AssertionError("No clue")


    def purchase_price(self):
        """A method to define real price.

        :returns: float -- price.
        """
        return self.price - (0.1 * self.mileage)


class Car(Vehicle):
    """Class to represent vehicle car.
    """
    wheels = 4


    def __init__(self, name, model, date_of_birth, mileage, price):
        """Create instance of car.

        :param model: model of car.
        :param model: str
        :param date_of_birth: data of release.
        :param date_of_birth: int.
        :param mileage: amount of distance in km.
        :param mileage: int.
        :param price: starting price.
        :param price: int.
        :param name: name of a car
        :param name: str
        :returns: Car -- instance of car.
        :raises: TypeError.
        """
        super().__init__(model, date_of_birth, mileage, price)
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.name = name


    def vehicle_type(self):
        """A method to show type, name and model of car.

        :returns: str.
        """
        return f"Car name {self.name} and model {self.model} "


class Motorcycle(Vehicle):
    """Class to represent vehicle - motorcycle.
    """
    wheels = 2

    def __init__(self, name, model, date_of_birth, mileage, price):
        """Create instance of motorcycle.

        :param model: model of motorcycle.
        :param model: str
        :param date_of_birth: data of release.
        :param date_of_birth: int.
        :param mileage: amount of distance in km.
        :param mileage: int.
        :param price: starting price.
        :param price: int.
        :param name: name of a motorcycle
        :param name: str
        :returns: Motorcycle -- instance of motorcycle.
        :raises: TypeError.
        """
        super().__init__(model, date_of_birth, mileage, price)
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.name = name

    def vehicle_type(self):
        """A method to show type, name and model of car.

        :returns: str.
        """
        return f"Motorcycle name {self.name} and model {self.model} "


class Truck(Vehicle):
    """Class to represent vehicle - truck.
    """
    wheels = 8


    def vehicle_type(self):
        """A method to show type, name and model of truck.

        :returns: str.
        """
        return f"Truck model {self.model} "


class Bus(Vehicle):
    """Class to represent vehicle - bus.
    """
    wheels = 6


    def vehicle_type(self):
        """A method to show type, name and model of bus.

        :returns: str.
        """
        return f"Bus model {self.model} "


if __name__ == "__main__":
    car1 = Car("Some_car_name", 'Some_car_model', 2009, 300, 500)
    print(car1.vehicle_type())
    print(car1.purchase_price())
    print(car1.is_motorcycle())
    moto1 = Motorcycle("Some_moto_name", "Some_moto_model", 2012, 500, 100)
    print(moto1.vehicle_type())
    print(moto1.purchase_price())
    print(moto1.is_motorcycle())
    truck1 = Truck("Some_truck_model", 2000, 45, 500)
    print(truck1.vehicle_type())
    print(truck1.purchase_price())
    print(truck1.is_motorcycle())
    bus1 = Bus("Some_bus_model", 2100, 0, 300)
    print(bus1.vehicle_type())
    print(bus1.purchase_price())
    print(bus1.is_motorcycle())
