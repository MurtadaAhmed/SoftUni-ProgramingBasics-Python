number = int(input())
total_combinations = 0
for number1 in range(0, number + 1):  # we start from 0 because the task asks for this
    for number2 in range(0, number + 1):
        for number3 in range(0, number + 1):
            if number1 + number2 + number3 == number:
                total_combinations += 1
print(total_combinations)