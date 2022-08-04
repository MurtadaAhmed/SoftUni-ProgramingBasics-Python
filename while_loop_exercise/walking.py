steps = 10000
command = input()
count_of_steps = 0
steps_is_reached = False
while command != "Going home":
    command = int(command)  # converting the value into integer
    count_of_steps += command
    if count_of_steps >= steps:
        steps_is_reached = True
        break
    command = input()

if command == "Going home":
    command = int(input())  # just one more reading after (going home)
    count_of_steps += command
    if count_of_steps >= steps:
        steps_is_reached = True

if steps_is_reached:
    print("Goal reached! Good job!")
    print(f"{count_of_steps - steps} steps over the goal!")
else:
    print(f"{steps - count_of_steps} more steps to reach goal.")
