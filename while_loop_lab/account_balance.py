entered_value = input()
total_sum = 0
while entered_value != "NoMoreMoney":
    entered_value = float(entered_value)  # here we convert the entered value into float
    if entered_value < 0:  # here we enter the condition for - value
        print("Invalid operation!")
        break
    else:  # here we continue with the positive values
        total_sum += entered_value  # here we add the entered value to the total sum
        print(f"Increase: {entered_value:.2f}")
        entered_value = input()
print(f"Total: {total_sum:.2f}")
