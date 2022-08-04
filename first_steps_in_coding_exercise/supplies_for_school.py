number_of_pens = int(input())
number_of_markers = int(input())
number_of_liters = int(input())
discount_percent = int(input())
price_of_pens = number_of_pens * 5.80
price_of_markers = number_of_markers * 7.20
price_of_liters = number_of_liters * 1.20
total_undiscounted = price_of_pens + price_of_markers + price_of_liters
total_discounted = total_undiscounted - (total_undiscounted * (discount_percent / 100))
print(total_discounted)