teniski_price = float(input())
winning_price = float(input())

shorti_price = teniski_price * 0.75
chorapi_price = shorti_price * 0.20
botonki_price = (teniski_price + shorti_price) * 2

total_price = teniski_price + shorti_price + chorapi_price + botonki_price

total_discounted_price = 0.85 * total_price

if total_discounted_price >= winning_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_discounted_price:.2f} lv.")
else:
    difference = winning_price - total_discounted_price
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")