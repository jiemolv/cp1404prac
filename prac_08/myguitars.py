# myguitars.py

from guitar import Guitar

def display_guitars(guitars):
    if not guitars:
        print("No guitars in the collection.")
    else:
        for i, guitar in enumerate(guitars):
            print(f"Guitar {i+1}: {guitar}")

def add_guitar(guitars):
    name = input("Enter the name: ")
    year = int(input("Enter the year: "))
    cost = float(input("Enter the cost: "))

    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print("Guitar added successfully!")

def write_guitars_to_file(guitars):
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("Guitars written to file.")

def read_guitars_from_file():
    guitars = []
    try:
        with open("guitars.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, year, cost = line.strip().split(",")
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
        pass
    return guitars

def main():
    guitars = read_guitars_from_file()

    while True:
        print("- (D)isplay guitars")
        print("- (A)dd guitar")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'd':
            display_guitars(guitars)
        elif choice == 'a':
            add_guitar(guitars)
        elif choice == 'q':
            write_guitars_to_file(guitars)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
