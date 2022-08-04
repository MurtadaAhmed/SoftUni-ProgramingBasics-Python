nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
price_nylon = (nylon + 2) * 1.50
price_paint = (paint + (paint*0.10)) * 14.50
price_thinner = thinner * 5.00
total_price_without_workers = price_nylon + price_paint + price_thinner + 0.40
price_workers = (total_price_without_workers * 0.30) * hours
final_price = total_price_without_workers + price_workers
print(final_price)