days = int(input())
accommodation = input()
rating = input()

nights = days - 1

if accommodation == "room for one person":
    price = nights * 18.00
elif accommodation == "apartment":
    price = nights * 25.00
    if days < 10:
        price = price * 0.70
    elif 10 <= days <= 15:
        price = price * 0.65
    elif days > 15:
        price = price * 0.50

elif accommodation == "president apartment":
    price = nights * 35.00
    if days < 10:
        price = price * 0.90
    elif 10 <= days <= 15:
        price = price * 0.85
    elif days > 15:
        price = price * 0.80

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.90

print(f"{price:.2f}")