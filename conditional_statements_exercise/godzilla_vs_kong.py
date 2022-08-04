budget = float(input())
number_extra = int(input())
price_cloth_per_one_extra = float(input())

decor_price = budget * 0.10

price_cloth = price_cloth_per_one_extra * number_extra

if number_extra > 150:
    price_cloth = price_cloth * 0.90

total_expenses = decor_price + price_cloth

difference_in_price = abs(budget - total_expenses)

if budget < total_expenses:
    print("Not enough money!")
    print(f"Wingard needs {difference_in_price:.2f} leva more.")
else:
    print("Action!""")
    print(f"Wingard starts filming with {difference_in_price:.2f} leva left.")