days = int(input())
accommodation = input()
rating = input()
price = 0
nights = days - 1
if accommodation == "room for one person":
    price = nights * 18.00
elif accommodation == "apartment":
    price = nights * 25.00
    if nights < 10:
        price = price * 0.70
    elif 10 <= nights <= 15:
        price = price * 0.65
    else:
        price = price * 0.50
elif accommodation == "president apartment":
    price = nights * 35.00
    if nights < 10:
        price = price * 0.90
    elif 10 <= nights <= 15:
        price = price * 0.85
    else:
        price = price * 0.80

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.90

print(f"{price:.2f}")
