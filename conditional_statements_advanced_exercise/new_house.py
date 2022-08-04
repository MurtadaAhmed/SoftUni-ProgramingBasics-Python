type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_of_flower == "Roses":
    price = 5
    price = number_of_flowers * price
    if number_of_flowers > 80:
        price = price * 0.90
elif type_of_flower == "Dahlias":
    price = 3.80
    price = number_of_flowers * price
    if number_of_flowers > 90:
        price = price * 0.85
elif type_of_flower == "Tulips":
    price = 2.80
    price = number_of_flowers * price
    if number_of_flowers > 80:
        price = price * 0.85
elif type_of_flower == "Narcissus":
    price = 3
    price = number_of_flowers * price
    if number_of_flowers < 120:
        price = price * 1.15
elif type_of_flower == "Gladiolus":
    price = 2.50
    price = number_of_flowers * price
    if number_of_flowers < 80:
        price = price * 1.20

difference_in_price = abs(budget-price)

if price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {difference_in_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference_in_price:.2f} leva more.")