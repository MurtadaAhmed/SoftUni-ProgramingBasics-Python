number_of_attempts = int(input()) # number of attempts to be used
even_numbers_sum = 0
odd_numbers_sum = 0

# we will check the sum for each the even and the odd numbers
for sum in range(1, number_of_attempts + 1):
    entered_number = int(input())
    if sum % 2 == 0:
        even_numbers_sum += entered_number
    else:
        odd_numbers_sum += entered_number

if even_numbers_sum == odd_numbers_sum:
    print("Yes")
    print(f"Sum = {odd_numbers_sum}") # we can put the even_numbers_sum as well as they both are equal
else:
    difference = abs(even_numbers_sum - odd_numbers_sum)
    print("No")
    print(f"Diff = {difference}")