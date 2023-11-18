num_items = int(input("Quantity of commodity："))

total_price = 0
for i in range(num_items):
    item_price = float(input("price of commodities："))
    total_price += item_price
print(f"{num_items} The total price of the goods is {total_price:.2f} U.S.DOLLAR")
