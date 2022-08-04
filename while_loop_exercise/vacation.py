required_money = float(input())
available_money = float(input())

spend_count = 0
days_count = 0

while available_money < required_money and spend_count < 5:
    action = input()
    amount = float(input())
    days_count += 1
    if action == "spend":
        available_money -= amount
        spend_count += 1
        if available_money < 0:
            available_money = 0
    elif action == "save":
        available_money += amount
        spend_count = 0  # we make the value zero here because we are looking for the condition...
# ...with 5 consequential days spending

if spend_count == 5:
    print("You can't save the money.")
    print(days_count)

if available_money >= required_money:
    print(f"You saved the money for {days_count} days.")
