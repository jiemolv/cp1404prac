# Question 1: Write user's name to a file

name = input("Please enter your name: ")  # Ask user for their name
with open('name.txt', 'w') as file:
    file.write(name)  # Write the name to the file

# Question 2: Read the name from the file and print it

with open('name.txt', 'r') as file:
    name = file.read()  # Read the name from the file
    print(f"Your name is {name}")  # Print the name

# Question 3: Read the first two numbers from numbers.txt and add them together

with open('numbers.txt', 'r') as file:
    numbers = file.readlines()  # Read all lines from the file
    num1 = int(numbers[0])  # First number
    num2 = int(numbers[1])  # Second number
    total = num1 + num2
    print("The total of the first two numbers is:", total)

# Question 4: Read all numbers from numbers.txt and calculate the total

with open('numbers.txt', 'r') as file:
    numbers = file.readlines()  # Read all lines from the file
    total = 0
    for number in numbers:
        total += int(number)  # Convert the number to int and add to total

print("The total of all numbers is:", total)
