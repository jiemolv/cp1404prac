# Constants
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

# Function to check if a string has at least one lowercase character
def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

# Function to check if a string has at least one uppercase character
def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

# Function to check if a string has at least one digit
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

# Function to check if a string has at least one special character
def has_special_character(password):
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False

# Main program
while True:
    password = input("Please enter a valid password: ")

    # Check password length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print(f"Invalid password! Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters.")
        continue

    # Check lowercase
    if not has_lowercase(password):
        print("Invalid password! Your password must contain at least one lowercase letter.")
        continue

    # Check uppercase
    if not has_uppercase(password):
        print("Invalid password! Your password must contain at least one uppercase letter.")
        continue

    # Check digit
    if not has_digit(password):
        print("Invalid password! Your password must contain at least one digit.")
        continue

    # Check special character
    if not has_special_character(password):
        print("Invalid password! Your password must contain at least one special character.")
        continue

    # If all checks pass, the password is valid
    print(f"Your {len(password)} character password is valid: {password}")
    break
