# total_income.py

def calculate_total_income(incomes, number_of_months):
    total = sum(incomes)
    average = total / number_of_months
    return total, average


def print_report(total, average):
    print(f"Total income: {total}")
    print(f"Average monthly income: {average}")


def main():
    incomes = []
    number_of_months = int(input("Enter the number of months: "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter the income for month {month}: "))
        incomes.append(income)

    total, average = calculate_total_income(incomes, number_of_months)
    print_report(total, average)


if __name__ == "__main__":
    main()
