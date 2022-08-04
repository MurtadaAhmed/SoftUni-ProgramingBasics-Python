amount_in_lev = float(input())  # in leva
# now we need to convert the leva into coins
coins = round(amount_in_lev * 100)  # we use round her to avoid having decimal points in the number
number_of_coins = 0
# in bulgaria we have the following coins : 2lv, 1lv, 50, 20, 10, 5, 2, 1

while coins > 0:
    if coins >= 200:  # for 2lv
        coins = coins - 200  # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 100:  # for 1lv
        coins = coins - 100 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 50:  # for 50
        coins = coins - 50 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 20:  # for 20
        coins = coins - 20 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 10:  # for 10
        coins = coins - 10 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 5:  # for 5
        coins = coins - 5 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 2:  # for 2
        coins = coins - 2 # we remove it from the total coins
        number_of_coins += 1
    elif coins >= 1:  # for 1
        coins = coins - 1 # we remove it from the total coins
        number_of_coins += 1
print(number_of_coins)