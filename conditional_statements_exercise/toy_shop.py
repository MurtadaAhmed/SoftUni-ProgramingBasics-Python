trip_price = float(input())
puzzle_number = int(input())
talkingdolls_number = int(input())
teadybear_number = int(input())
minion_number = int(input())
truck_number = int(input())

price = (puzzle_number * 2.60) + (talkingdolls_number * 3) + (teadybear_number * 4.100) + (minion_number * 8.20) + (truck_number * 2)

number_toys = puzzle_number + talkingdolls_number + teadybear_number + minion_number + truck_number

if number_toys >= 50:
    price = price * 0.75  # earning with discount

price = price * 0.90  # earning without rent

difference = abs(price - trip_price)  # abs is to get the price difference without negative value

if price >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")