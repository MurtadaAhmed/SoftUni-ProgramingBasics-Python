# 1- we enter the number of the groups
# 2- we loop through each group with the number of people for each one of them
# 3- based on the number we can categorize them into the mountains that they will climb
# 4- we count the number of people for each group and we take the percentage

number_of_groups = int(input())

number_of_people_musala = 0
number_of_people_monblan = 0
number_of_people_kilimanjaro = 0
number_of_people_k2 = 0
number_of_people_evrest = 0

# now we enter the loop to count how many people in each group and to add them in their perspective group count
for number in range(1, number_of_groups + 1):
    number_of_people = int(input())
    if number_of_people <= 5:
        number_of_people_musala += number_of_people
    elif number_of_people <= 12:
        number_of_people_monblan += number_of_people
    elif number_of_people <= 25:
        number_of_people_kilimanjaro += number_of_people
    elif number_of_people <= 40:
        number_of_people_k2 += number_of_people
    elif number_of_people >= 41:
        number_of_people_evrest += number_of_people

# now we count the total number of people in all groups so we can count the percentage after that
total_number_of_people = number_of_people_musala + number_of_people_monblan + number_of_people_kilimanjaro + number_of_people_k2 + number_of_people_evrest

# now we count the percentage for each group

percent_musala = (number_of_people_musala / total_number_of_people) * 100
percent_monblan = (number_of_people_monblan / total_number_of_people) * 100
percent_kilimanjaro = (number_of_people_kilimanjaro/ total_number_of_people) * 100
percent_k2 = (number_of_people_k2 / total_number_of_people) * 100
percent_evrest = (number_of_people_evrest / total_number_of_people) * 100

# now we print them with the formatting and add %
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_evrest:.2f}%")


