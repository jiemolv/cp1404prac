from guitar import Guitar

def load_guitars_from_file(file_name):
    """Read guitars from file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return guitars

def write_guitars_to_file(file_name, guitars):
    """Write guitars to a file."""
    try:
        with open(file_name, 'w') as file:
            for guitar in guitars:
                file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    except IOError:
        print(f"Error writing to file '{file_name}'.")

def main():
    file_name = 'guitars.csv'
    guitars = load_guitars_from_file(file_name)
    print("List of guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    print("\nEnter details of new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    write_guitars_to_file(file_name, guitars)
    print("\nNew guitar added and saved to file.")

if __name__ == "__main__":
    main()
