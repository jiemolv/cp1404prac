from taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100),
             Taxi("Camry", 120),
             Taxi("Corolla", 80)]

    total_bill = 0

    print("Available Taxis:")
    display_taxis(taxis)

    menu_choice = get_menu_choice()

    while menu_choice != "q":
        if menu_choice == "d":
            drive_taxi(taxis)
        else:
            print("Invalid choice")

        print()
        menu_choice = get_menu_choice()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """
    Display available taxis.
    """
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def get_menu_choice():
    """
    Get and return the menu choice from the user.
    """
    print("Menu:")
    print("d) drive")
    print("q) quit")
    return input(">>> ").lower()


def drive_taxi(taxis):
    """
    Drive a taxi and calculate the fare.
    """
    taxi_choice = get_taxi_choice(taxis)
    distance = get_positive_number("Drive how far? ")
    taxi = taxis[taxi_choice]
    taxi.start_fare()
    taxi.drive(distance)
    fare = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, fare))


def get_taxi_choice(taxis):
    """
    Get and return the taxi choice from the user.
    """
    display_taxis(taxis)
    taxi_choice = get_positive_number("Choose taxi: ")
    while taxi_choice >= len(taxis):
        print("Invalid taxi choice.")
        taxi_choice = get_positive_number("Choose taxi: ")
    return taxi_choice


def get_positive_number(prompt):
    """
    Get a positive number from the user and return it.
    """
    number = float(input(prompt))
    while number < 0:
        print("Number must be >= 0")
        number = float(input(prompt))
    return number


if __name__ == "__main__":
    main()
