seat_type = input()
number_of_rows = int(input())
number_of_columns = int(input())
price = 0
if seat_type == "Premiere":
    price = 12.00
elif seat_type == "Normal":
    price = 7.50
elif seat_type == "Discount":
    price = 5.00
total_number_of_seats = number_of_columns * number_of_rows
price = price * total_number_of_seats
print(f"{price:.2f} leva")
