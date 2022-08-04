number_of_inputs = int(input())
number = int(input())  # we put it outside the "for" loop so we can set a default value...
# ... number for comparison later
minimum_number = number
maximum_number = number
for repeat in range(1, number_of_inputs):
    new_number = int(input())
    if new_number > maximum_number:
        maximum_number = new_number  # this will enter the loop until it get set to the maximum value
    if new_number < minimum_number:  # this is a separate "if" so we can loop through the all numbers until we set it
        # to the minimum one
        minimum_number = new_number

print(f"Max number: {maximum_number}")
print(f"Min number: {minimum_number}")
