first_number = int(input())
second_number = int(input())
magic_number = int(input())
total_combinations = 0
is_found = False
for number1 in range(first_number, second_number + 1):
    for number2 in range(first_number, second_number + 1):
        total_combinations += 1
        if number1 + number2 == magic_number:
            is_found = True
            print(f"Combination N:{total_combinations} ({number1} + {number2} = {magic_number})")
            break
    if is_found:  # to break the whole cycle in case the combination is found
        break

if not is_found:
    print(f"{total_combinations} combinations - neither equals {magic_number}")

