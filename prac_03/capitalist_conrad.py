import random

# Constants
STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
OUTPUT_FILE = 'stock_prices.txt'

def main():
    price = STARTING_PRICE
    day = 1

    out_file = open(OUTPUT_FILE, 'w')
    print(f"Starting price: ${price:.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        price_change = 0
        # Generate a random number between 0 and 1
        if random.randint(0, 1) == 0:
            # Decrease the price
            price_change = random.uniform(0, MAX_DECREASE)
            price *= (1 - price_change)
        else:
            # Increase the price
            price_change = random.uniform(0, MAX_INCREASE)
            price *= (1 + price_change)

        # Display the price to the nearest cent
        formatted_price = "${:,.2f}".format(price)
        print(f"On day {day} price is: {formatted_price}", file=out_file)

        day += 1

    out_file.close()

if __name__ == '__main__':
    main()
