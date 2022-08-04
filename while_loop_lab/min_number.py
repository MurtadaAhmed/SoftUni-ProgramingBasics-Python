import sys
entered_value = input()
minimum_number = sys.maxsize
while entered_value != "Stop":
    entered_value = int(entered_value)  # convert the entered value into integer
    if entered_value < minimum_number:
        minimum_number = entered_value
    entered_value = input()

print(minimum_number)