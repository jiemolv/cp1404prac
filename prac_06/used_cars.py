from prac_06.car import Car

def main():
    # create a new Car object called "my_car" and set its fuel to 0
    my_car = Car("Car", 0)

    # add 20 units of fuel to my_car using the add method
    my_car.add_fuel(20)

    # print the amount of fuel in my_car
    print(f"Amount of fuel in {my_car.name}: {my_car.fuel}")

    # attempt to drive my_car 115 km
    distance = 115
    if my_car.drive(distance):
        print(f"{my_car.name} drove {distance} km")
    else:
        print(f"{my_car.name} could not drive {distance} km")

    # create another Car object called "limo" and set its fuel to 100
    limo = Car("Limo", 100)

    # add 20 units of fuel to limo using the add method
    limo.add_fuel(20)

    # print the amount of fuel in limo
    print(f"Amount of fuel in {limo.name}: {limo.fuel}")

    # attempt to drive limo 115 km
    distance = 115
    if limo.drive(distance):
        print(f"{limo.name} drove {distance} km")
    else:
        print(f"{limo.name} could not drive {distance} km")

    # print the string representation of my_car and limo
    print(str(my_car))
    print(str(limo))

if __name__ == '__main__':
    main()
