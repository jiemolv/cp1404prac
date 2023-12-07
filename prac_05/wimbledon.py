import csv

def read_wimbledon_data(filename):
    """Reads the Wimbledon data from the provided CSV file and returns the data as a list of lists."""
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            wimbledon_data.append(row)
    return wimbledon_data

def get_champions_and_counts(wimbledon_data):
    """Processes the Wimbledon data to get the champions and how many times they have won."""
    champions_counts = {}
    for row in wimbledon_data:
        champion = row[1]
        if champion in champions_counts:
            champions_counts[champion] += 1
        else:
            champions_counts[champion] = 1
    return champions_counts

def get_countries_of_champions(wimbledon_data):
    """Processes the Wimbledon data to get the countries of the champions in alphabetical order."""
    countries = {row[2] for row in wimbledon_data}
    return sorted(countries)

def display_champions(champions_counts):
    """Displays the champions and how many times they have won."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champions_counts.items()):
        print(f"{champion} {count}")

def display_countries(countries):
    """Displays the countries of the champions in alphabetical order."""
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    filename = 'wimbledon.csv'
    wimbledon_data = read_wimbledon_data(filename)
    champions_counts = get_champions_and_counts(wimbledon_data)
    countries = get_countries_of_champions(wimbledon_data)
    display_champions(champions_counts)
    display_countries(countries)

if __name__ == "__main__":
    main()
