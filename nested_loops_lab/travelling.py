total_saved = 0
amount_is_reached = False
command = input()
while command != "End":
    minimum_budget = float(input())
    amount_is_reached = False
    while not amount_is_reached:

        money_saved = float(input())
        total_saved += money_saved
        if total_saved >= minimum_budget:
            amount_is_reached = True
            print(f"Going to {command}!")
            break
    total_saved = 0  # to retrun to the default value for the next destination calculation
    command = input()


