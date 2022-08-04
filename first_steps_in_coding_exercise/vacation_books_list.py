pages_numbers = int(input())
pages_per_hour = int(input())
days = int(input())
total_hours_needed = pages_numbers // pages_per_hour
hours_per_day = total_hours_needed // days
print(hours_per_day)