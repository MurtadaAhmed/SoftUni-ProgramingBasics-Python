width = int(input())
length = int(input())
height = int(input())

apartment_volume = width * length * height
total_size_of_bags = 0
command_or_number_of_bags = int(input())  # str because it might include the word Done

while command_or_number_of_bags != "Done":
    command_or_number_of_bags = int(command_or_number_of_bags)  # convert str into int
    total_size_of_bags += command_or_number_of_bags
    if total_size_of_bags >= apartment_volume:
        break
    command_or_number_of_bags = input()

difference = abs(apartment_volume - total_size_of_bags)

if command_or_number_of_bags == "Done":
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")