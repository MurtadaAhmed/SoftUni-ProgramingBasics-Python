budget = float(input())
videocard_number = int(input())
processor_number = int(input())
ram_number = int(input())
price_videocard = videocard_number * 250
price_processor = processor_number * (price_videocard * 0.35)
price_ram = ram_number * (price_videocard * 0.10)
total_price = price_videocard + price_processor + price_ram
if videocard_number > processor_number:
    total_price = total_price * 0.85
price_difference = abs(budget - total_price)
if total_price > budget:
    print(f"Not enough money! You need {price_difference:.2f} leva more!")
else:
    print(f"You have {price_difference:.2f} leva left!")