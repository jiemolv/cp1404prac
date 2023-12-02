# Prompting user for 5 numbers and storing them in a list called numbers
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Outputting information about these numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_username = input("Enter your username: ")
if input_username in usernames:
    print("Access granted")
else:
    print("Access denied")
