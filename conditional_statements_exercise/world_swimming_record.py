world_record = float(input())
distance_meter = float(input())
seconds_for_one_meter = float(input())
seconds_for_all_meters = distance_meter * seconds_for_one_meter
number_of_delays = distance_meter//15
seconds_delay = number_of_delays * 12.5
seconds_for_all_meters = seconds_for_all_meters + seconds_delay  # added the delay
if seconds_for_all_meters >= world_record:
    delay_from_record = seconds_for_all_meters - world_record
    print(f"No, he failed! He was {delay_from_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {seconds_for_all_meters:.2f} seconds.")
