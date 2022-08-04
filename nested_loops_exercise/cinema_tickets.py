command = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
student_total_count = 0
standard_total_count = 0
kid_total_count = 0
seats_total_count = 0
while command != "Finish":  # it means that we are reading the name of the film
    seats_count = 0
    available_seats = int(input())
    type_of_ticket = input()
    student_ticket = 0
    standard_ticket = 0
    kid_ticket = 0

    while type_of_ticket != "End":

        if type_of_ticket == "student":
            student_ticket += 1
            seats_count += 1
            student_total_count += 1
            seats_total_count += 1
        elif type_of_ticket == "standard":
            standard_ticket += 1
            seats_count += 1
            standard_total_count += 1
            seats_total_count += 1
        elif type_of_ticket == "kid":
            kid_ticket += 1
            seats_count += 1
            kid_total_count += 1
            seats_total_count += 1

        if available_seats == seats_count:
            print(f"{command} - {((seats_count / available_seats) * 100):.2f}% full.")
            break

        type_of_ticket = input()

    if type_of_ticket == "End":
        print(f"{command} - {((seats_count / available_seats) * 100):.2f}% full.")
    command = input()

kid_percent = (kid_total_count / seats_total_count) * 100
standard_percent = (standard_total_count / seats_total_count) * 100
student_percent = (student_total_count / seats_total_count) * 100
print(f"Total tickets: {seats_total_count}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
