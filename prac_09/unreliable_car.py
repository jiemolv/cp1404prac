from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car with reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance, based on parent class Car.
        Set the reliability to the value passed in.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the UnreliableCar if a random number is less than the car's reliability.
        Return the distance driven if the car was able to drive, 0 otherwise.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
