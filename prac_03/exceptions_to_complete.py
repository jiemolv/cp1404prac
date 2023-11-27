while True:
    try:
        # Get an integer from the user
        num = int(input("Enter an integer: "))

        # TODO: Complete the program according to the instructions in the comments

        # Print the square of the number
        result = num ** 2
        print(f"The square of {num} is {result}")

        # Exit the loop
        break

    except ValueError:
        # Handle the exception when a non-number is entered
        print("Invalid input. Please enter an integer.")
