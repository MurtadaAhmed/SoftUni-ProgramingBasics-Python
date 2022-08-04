import sys
entered_value = input()
maximum_number = - sys.maxsize
while entered_value != "Stop":
    entered_value = int(entered_value)  # convert the entered value into integer
    if entered_value > maximum_number:
        maximum_number = entered_value
    entered_value = input()

print(maximum_number)