def calculate_bonus(sales):
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    return bonus

def main():
    while True:
        sales = float(input("Enter sales: $"))
        if sales < 0:
            break
        bonus = calculate_bonus(sales)
        print(f"Based on the sales of ${sales:.2f}, your bonus is ${bonus:.2f}.")

if __name__ == "__main__":
    main()
