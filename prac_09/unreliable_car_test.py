from unreliable_car import UnreliableCar

# Create a new unreliable car object with a reliability of 50%
my_car = UnreliableCar("Unreliable Car", 100, 50)

# Drive the car 50 km, which should be successful half of the time
distance_driven = my_car.drive(50)
print("Distance Driven:", distance_driven)

# Drive the car 100 km, which should fail more often than not
distance_driven = my_car.drive(100)
print("Distance Driven:", distance_driven)
