CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
