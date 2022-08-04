# we read the number of people
# outer cycle >> to read the text until we reach the command Finish and the cycle length with the number of people
# inner cycle >> we read the degree for each text for the number of people

number_of_people = int(input())
degrees_count = 0
degrees_all_presentation = 0
command = input()
counter = 0
while command != "Finish":  # then it will read the name of the presentation
    total_degrees_per_presentation = 0
    presentation = command
    for i in range(0, number_of_people):  # read the grades for each presentation
        degree = float(input())
        total_degrees_per_presentation += degree
        degrees_all_presentation += degree
        degrees_count += 1
    average_grade = total_degrees_per_presentation / number_of_people
    print(f"{presentation} - {average_grade:.2f}.")

    command = input()
average_all_presentation = degrees_all_presentation / degrees_count
print(f"Student's final assessment is {average_all_presentation:.2f}.")


