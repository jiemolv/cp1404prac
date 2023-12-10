from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013)

# Test get_age()
expected_age1 = 100
age1 = guitar1.get_age()
print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {age1}")

expected_age2 = 9
age2 = guitar2.get_age()
print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {age2}")

# Test is_vintage()
expected_vintage1 = True
vintage1 = guitar1.is_vintage()
print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {vintage1}")

expected_vintage2 = False
vintage2 = guitar2.is_vintage()
print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {vintage2}")
