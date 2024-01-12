from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with different pricing based on fanciness."""

    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        """
        Initialise a SilverServiceTaxi instance, based on parent class Taxi.
        Multiply the price_per_km by the fanciness value.
        """
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """
        Calculate the fare for the current trip by adding the total distance driven
        multiplied by the price_per_km, and adding the flagfall amount.
        """
        return (super().get_fare() + self.flagfall)

    def __str__(self):
        """
        Return a string representation of the SilverServiceTaxi, including the flagfall.
        """
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

