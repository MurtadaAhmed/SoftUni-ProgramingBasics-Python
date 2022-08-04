number_of_attempts = int(input())
# now we set the default value of numbers for each group:
first_group_count = 0
second_group_count = 0
third_group_count = 0
fourth_group_count = 0
fifth_group_count = 0

# now we enter the loop to add the count for each group
for number in range(1, number_of_attempts + 1):
    number = int(input())

    if number < 200:
        first_group_count += 1
    elif number <= 399:
        second_group_count += 1
    elif number <= 599:
        third_group_count += 1
    elif number <= 799:
        fourth_group_count += 1
    elif number >= 800:
        fifth_group_count += 1

#  now we will count the percentage for each group

first_group_percent = first_group_count / number_of_attempts * 100
second_group_percent = second_group_count / number_of_attempts * 100
third_group_percent = third_group_count / number_of_attempts * 100
fourth_group_percent = fourth_group_count / number_of_attempts * 100
fifth_group_percent = fifth_group_count / number_of_attempts * 100

#  now we print the percentages
print(f"{first_group_percent:.2f}%")
print(f"{second_group_percent:.2f}%")
print(f"{third_group_percent:.2f}%")
print(f"{fourth_group_percent:.2f}%")
print(f"{fifth_group_percent:.2f}%")
