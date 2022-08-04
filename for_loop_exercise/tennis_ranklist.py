import math
number_of_tournaments = int(input())
initial_rank = int(input())
total_points = 0
number_of_wins = 0
for i in range(1, number_of_tournaments + 1):
    reached_level_of_tournament = input()
    if reached_level_of_tournament == "W":
        total_points += 2000
        number_of_wins += 1  # to calculate the number of wins
    elif reached_level_of_tournament == "F":
        total_points += 1200
    elif reached_level_of_tournament == "SF":
        total_points += 720

initial_plus_total = initial_rank + total_points
average_point = math.floor(total_points / number_of_tournaments)
percent_of_wins = (number_of_wins / number_of_tournaments) * 100

# finally we need to print the results
print(f"Final points: {initial_plus_total}")
print(f"Average points: {average_point}")
print(f"{percent_of_wins:.2f}%")

