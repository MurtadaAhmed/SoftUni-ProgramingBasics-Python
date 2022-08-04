import math
from math import ceil
name_of_serial = input()
episode_duration = int(input())
break_duration = int(input())

lunch_break = break_duration / 8
rest_break = break_duration / 4

break_remaining = break_duration - lunch_break - rest_break
the_last_remaining = abs(break_remaining - episode_duration)

if break_remaining >= episode_duration:
    print(f"You have enough time to watch {name_of_serial} and left with {math.ceil(the_last_remaining)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(the_last_remaining)} more minutes.")
