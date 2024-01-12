from silver_service_taxi import SilverServiceTaxi

# Create a new SilverServiceTaxi object with a fanciness of 2
my_taxi = SilverServiceTaxi("Hummer", 200, 4.92, 2)

# Drive the taxi for 18 km
my_taxi.drive(18)

# Calculate and print the fare
fare = my_taxi.get_fare()
print("Fare:", fare)
