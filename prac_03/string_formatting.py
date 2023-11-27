# Example of f-string formatting
brand = "Gibson"
model = "L-5 CES"
year = 1922
cost = 16035
output = f"{year} {brand} {model} for about ${cost:,}!"
print(output)

# Using a for loop with range function and string formatting
for i in range(0, 201, 50):
    print(f"{i:>3}")
