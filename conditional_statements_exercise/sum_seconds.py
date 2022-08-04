first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())
total_seconds = first_competitor + second_competitor + third_competitor
total_minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
if remaining_seconds < 10:
    print(f"{total_minutes}:0{remaining_seconds}")
else:
    print(f"{total_minutes}:{remaining_seconds}")