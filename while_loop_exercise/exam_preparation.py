unsatisfactory_count = int(input())
number_of_tasks = 0
unsatisfactory_attempts = 0
is_unsatisfactory = True
total_grades = 0
name_of_last_task = ""
# in the while cycle when need to put in mind the condition for (enough) / grade <=4 / number of unsatisfactory attempts
while unsatisfactory_attempts < unsatisfactory_count:
    name_of_task = input()
    if name_of_task == "Enough":
        is_unsatisfactory = False
        break

    number_of_tasks += 1
    name_of_last_task = name_of_task
    grade = int(input())
    total_grades += grade
    if grade <=4:
        unsatisfactory_attempts += 1



if is_unsatisfactory:
    print(f"You need a break, {unsatisfactory_attempts} poor grades.")
else:
    print(f"Average score: {total_grades/number_of_tasks:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {name_of_last_task}")