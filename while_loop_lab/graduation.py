name = input()
student_class = 1
total_grades = 0
loss_attempts = 0
is_lost = False
while student_class <= 12:
    grade = float(input())
    if grade < 4:
        loss_attempts += 1
        if loss_attempts > 1:
            is_lost = True
            break
    else:
        total_grades += grade
        student_class += 1
if is_lost:
    print(f"{name} has been excluded at {student_class} grade")
else:
    print(f"{name} graduated. Average grade: {(total_grades/12):.2f}")