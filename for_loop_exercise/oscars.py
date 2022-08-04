# 1- enter actor name + points from academia + number of evaluators.
# 2- we enter the loop to check the name of the evaluator
# 3- we calculate the points in the loop : points from actor * length of the name / 2
# 4- if the result at one point reach 1250.5 , we need to cut the loop with a message
# 5 - otherwise we need to print the needed amount (1250.5 - total points)

actor_name = input()
points_from_academia = float(input())
number_of_evaluators = int(input())
total_points = points_from_academia  # we created this variable so we can amend its value in the loop
for i in range(1, number_of_evaluators +1 ):
    name_of_evaluator = input()
    initial_points_from_evaluator = float(input())
    total_points_from_evaluator = (len(name_of_evaluator) * initial_points_from_evaluator) / 2
    total_points = total_points + total_points_from_evaluator
    if total_points >= 1250.50:
        break

if total_points >= 1250.50:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.50 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")


