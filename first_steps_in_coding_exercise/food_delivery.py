chicken = int(input())
fish = int(input())
veg = int(input())
chicken_price = chicken * 10.35
fish_price = fish * 12.40
veg_price = veg * 8.15
price_without_desert = chicken_price + fish_price + veg_price
price_with_desert = price_without_desert + (price_without_desert*0.20)
total_price =  price_with_desert + 2.50
print(total_price)