number_count = int(input()) # the number of inputs for each left and right amounts
first_or_left_entered_sum = 0
second_or_right_entered_sum = 0

# now we will count the sum for the first entered numbers:
for count in range(1, number_count + 1):
    entered_number = int(input())
    first_or_left_entered_sum += entered_number

# now we will count the sum for the second entered numbers:
for count in range(1, number_count + 1):
    entered_number = int(input())
    second_or_right_entered_sum += entered_number

if first_or_left_entered_sum == second_or_right_entered_sum:
    print(f"Yes, sum = {first_or_left_entered_sum}") # here we can put the first or the second as both are equal
else:
    difference = abs(first_or_left_entered_sum - second_or_right_entered_sum)
    print(f"No, diff = {difference}")