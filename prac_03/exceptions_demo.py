#When will a ValueError occur?
#A ValueError will occur when the user enters a non-integer value for the numerator or denominator. This can happen if the user inputs a non-digit character or a decimal number.

#When will a ZeroDivisionError occur?
#A ZeroDivisionError will occur when the user enters a zero as the denominator. In mathematics, division by zero is not allowed and leads to an invalid operation.

#Could you change the code to avoid the possibility of a ZeroDivisionError? If you could figure out the answer to question 3, then make this change now.
#Yes, we can change the code to avoid the possibility of a ZeroDivisionError. We can add a condition to check if the denominator is zero before performing the division operation. If the denominator is zero, we can handle this case in the code and prompt the user to enter a non-zero denominator.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Division result:", result)
    except ValueError:
        print("A ValueError occurred.")
    except ZeroDivisionError:
        print("A ZeroDivisionError occurred.")


# Test Cases
divide_numbers(10, "5")
divide_numbers(10, 0)
divide_numbers(10, 2)
