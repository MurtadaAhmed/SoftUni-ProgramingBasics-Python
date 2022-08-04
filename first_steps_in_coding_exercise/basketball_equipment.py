yearly_tax = int(input())
price_shoes = yearly_tax - (yearly_tax * 0.40)
price_team = price_shoes - (price_shoes * 0.20)
price_ball = price_team / 4
price_access = price_ball / 5
total_price = yearly_tax + price_shoes + price_team + price_ball + price_access
print(total_price)