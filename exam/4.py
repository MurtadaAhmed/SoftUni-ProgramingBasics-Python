import math

days = int(input())
km_first_day = float(input())

total_km = km_first_day
totat_sum = km_first_day
for i in range(days):
    percent = int(input())
    percent = 1 + (percent / 100)
    total_km = total_km * percent
    totat_sum = totat_sum + total_km

difference = abs(totat_sum - 1000)
if totat_sum >= 1000:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")