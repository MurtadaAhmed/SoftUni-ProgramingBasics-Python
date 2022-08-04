# 1- we will enter the open tabs + salary amount 2- we enter the loop to check the name of the tabs + how much the
# salary will be after each one of them 3- we add to the loop that if the salary became <= 0 to cut the loop and
# print the message that they lost the salary, otherwise we need to enter the amount of the salary left

number_of_open_tabs = int(input())
salary = int(input())

for tab_number in range(1, number_of_open_tabs + 1):
    tab_name = input()
    if tab_name == "Facebook":
        salary = salary - 150
    elif tab_name == "Instagram":
        salary = salary - 100
    elif tab_name == "Reddit":
        salary = salary - 50
    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
