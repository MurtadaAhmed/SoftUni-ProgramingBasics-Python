number_of_tries = int(input()) # the total number of inputs
total_sum = 0
for number in range(1, number_of_tries + 1):
    number_input = int(input())
    total_sum += number_input
print(total_sum)