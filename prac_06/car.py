class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        fuel_required = distance / 10
        if fuel_required > self.fuel:
            return False
        else:
            self.fuel -= fuel_required
            self.odometer += distance
            return True

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
