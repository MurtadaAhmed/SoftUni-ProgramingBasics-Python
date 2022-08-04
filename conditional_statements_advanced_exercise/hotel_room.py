month = input()
nights = int(input())
price_studio = 0
price_flat = 0
if month == "May" or month == "October":
    price_studio = 50 * nights
    price_flat = 65 * nights
    if 7 < nights <= 14:
        price_studio = price_studio * 0.95
    elif nights > 14:
        price_studio = price_studio * 0.70
        price_flat = price_flat * 0.90

elif month == "June" or month == "September":
    price_studio = 75.20 * nights
    price_flat = 68.70 * nights
    if nights > 14:
        price_studio = price_studio * 0.80
        price_flat = price_flat * 0.90

elif month == "July" or month == "August":
    price_studio = 76 * nights
    price_flat = 77 * nights
    if nights > 14:
        price_flat = price_flat * 0.90

print(f"Apartment: {price_flat:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
