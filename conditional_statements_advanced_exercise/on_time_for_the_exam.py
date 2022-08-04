hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

# convert the hours into minutes
total_minutes_of_exam = (hour_of_exam * 60) + minutes_of_exam
total_minutes_of_arrival = (hour_of_arrival * 60) + minutes_of_arrival

# calculate the difference between exam and arrival minutes
differnce = abs(total_minutes_of_arrival - total_minutes_of_exam)

# Late, on time or early
if total_minutes_of_arrival > total_minutes_of_exam:
    print("Late")
    if differnce < 60:
        print(f"{differnce} minutes after the start")
    else:
        hour = differnce // 60
        minutes = differnce % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
elif total_minutes_of_arrival == total_minutes_of_exam:
    print("On time")
elif differnce <= 30:
    print("On time")
    print(f"{differnce} minutes before the start")
elif differnce > 30:
    print("Early")
    if differnce < 60:
        print(f"{differnce} minutes before the start")
    else:
        hour = differnce // 60
        minutes = differnce % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
