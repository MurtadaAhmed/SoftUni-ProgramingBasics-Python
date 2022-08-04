budget = int(input())
season = input()
number_of_fishers = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer":
    price = 4200
elif season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_of_fishers <= 6:
    price = price * 0.90
elif 7 <= number_of_fishers <=11:
    price = price * 0.85
elif number_of_fishers >= 12:
    price = price * 0.75

if number_of_fishers % 2 == 0:
    if season == "Spring" or season == "Summer" or season == "Winter":
        price = price * 0.95
price_difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {price_difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_difference:.2f} leva.")