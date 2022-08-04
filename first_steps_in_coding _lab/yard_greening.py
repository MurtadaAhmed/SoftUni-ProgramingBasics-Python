size = float(input())
price_without_discount = size * 7.61
discount = price_without_discount * 0.18
discounted_price = price_without_discount - discount
print(f'The final price is: {discounted_price} lv')
print(f'The discount is: {discount} lv.')