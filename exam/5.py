first_day = 5364
top = 8848
days = 1
total_count = first_day
command = input()
while command != "END":  # which means eiher yes or no
    if command == "Yes":
        days += 1
        if days > 5:
            break
        meters = int(input())
        total_count = total_count + meters
    elif command == "No":
        meters = int(input())
        total_count = total_count + meters
    if total_count >= top:
        break
    command = input()

if total_count >= top:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(total_count)