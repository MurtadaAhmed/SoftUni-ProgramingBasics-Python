age = int(input())
price_of_washing_machine = float(input())
price_of_one_toy = int(input())
number_of_evens_years = 0
number_of_odd_years = 0
money = 10  # here is the default value that we will increase with 10 for each loop
money_for_even_years = 0
money_for_odd_years = 0

#  now we enter the loop to see how much she calculated money + toys as per her age

for i in range(1, age + 1):  # now we count the even and odd years to calculate the money
    if i % 2 == 0:
        number_of_evens_years += 1
        money_for_even_years = money_for_even_years + money  # it will be 10 for the first even year
        money = money + 10  # here we increase its value by ten for each even year

    else:
        number_of_odd_years += 1

# now we count the money for the odd years
money_for_odd_years = number_of_odd_years * price_of_one_toy

# now we count how much her brother is taking from her even years
money_taken_by_brother = number_of_evens_years * 1  # one leva each even year

# now we count the total sum minus the money that her brother is taking
total_sum = (money_for_even_years + money_for_odd_years) - money_taken_by_brother

if total_sum >= price_of_washing_machine:
    money_left = total_sum - price_of_washing_machine
    print(f"Yes! {money_left:.2f}")
else:
    money_left = price_of_washing_machine - total_sum
    print(f"No! {money_left:.2f}")


