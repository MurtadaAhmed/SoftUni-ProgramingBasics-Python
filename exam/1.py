papers_amount = int(input())
fabric_amount = int(input())
glue_amount = float(input())
discount_percent = int(input())

papers_price = papers_amount * 5.80
price_fabric = fabric_amount * 7.20
glue_price = glue_amount * 1.20

total_price = papers_price + price_fabric + glue_price
discount = discount_percent / 100
dicounted_price = discount * total_price
final_price = total_price - dicounted_price

print(f"{final_price:.3f}")