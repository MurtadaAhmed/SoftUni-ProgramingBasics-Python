first_number = int(input())
second_number = int(input())
operator = input()
result = 0
even_or_odd = ""
zero_number = False
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/" and second_number != 0:
    result = first_number / second_number
elif operator == "%" and second_number != 0:
    result = first_number % second_number

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

if operator == "/" or operator == "%":
    if second_number == 0:
        zero_number = True

if operator == "+" or operator == "-" or operator == "*":
    print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator == "/" and zero_number is False:
    print(f"{first_number} {operator} {second_number} = {result:.2f}")
elif operator == "%" and zero_number is False:
    print(f"{first_number} {operator} {second_number} = {result}")
elif zero_number is True:
    print(f"Cannot divide {first_number} by zero")