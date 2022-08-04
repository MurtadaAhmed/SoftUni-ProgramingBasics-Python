import sys
number_of_inputs = int(input())
maximum_number = -sys.maxsize  # we put the maximum negative values to find the biggest number
total_sum = 0
for number in range(1, number_of_inputs + 1):
    number = int(input())
    total_sum += number  # here we count the total sum including the maximum  number
    if number > maximum_number:
        maximum_number = number

total_sum_without_maximum_number = total_sum - maximum_number

if total_sum_without_maximum_number == maximum_number:
    print("Yes")
    print(f"Sum = {maximum_number}")  # or we can use total_sum_without_maximum_number as they are equ
else:
    difference = abs(total_sum_without_maximum_number - maximum_number)
    print("No")
    print(f"Diff = {difference}")