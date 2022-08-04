city = input()
sale = float(input())
commision = 0
city_is_valid = True
sale_is_valid = True
if city == "Sofia":
    if 0 <= sale <= 500:
        commision = 0.05
    elif 500 < sale <= 1000:
        commision = 0.07
    elif 1000 < sale <= 10000:
        commision = 0.08
    elif sale > 10000:
        commision = 0.12
    else:
        sale_is_valid = False
        print("error")
elif city == "Varna":
    if 0 <= sale <= 500:
        commision = 0.045
    elif 500 < sale <= 1000:
        commision = 0.075
    elif 1000 < sale <= 10000:
        commision = 0.10
    elif sale > 10000:
        commision = 0.13
    else:
        sale_is_valid = False
        print("error")
elif city == "Plovdiv":
    if 0 <= sale <= 500:
        commision = 0.055
    elif 500 < sale <= 1000:
        commision = 0.08
    elif 1000 < sale <= 10000:
        commision = 0.12
    elif sale > 10000:
        commision = 0.145
    else:
        sale_is_valid = False
        print("error")
else:
    city_is_valid = False
    print("error")

if city_is_valid and sale_is_valid:
    final_price = sale * commision
    print(f"{final_price:.2f}")
