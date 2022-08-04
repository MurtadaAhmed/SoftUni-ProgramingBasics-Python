# 1- creating outer cycle to get all numbers in the range between the 2 numbers
# 2- creating inner cycle to get the sum of even and odd indexes of each number

start_number = int(input())
end_number = int(input())
# get the range of numbers:
for six_numbers in range(start_number, end_number + 1):
    # converting the number into string so we can get the length + index later:
    number_in_string = str(six_numbers)
    # adding the default values for the even + odd sums for each cycle:
    even_sum = 0
    odd_sum = 0
    # creating inner cycle for the length of the number (6 according to the task) + checking the index:
    for index in range(0, len(number_in_string)):
        # converting the number back into integer and add the index number according to the inner cycle:
        # it is converted to integer so we can add it to the total sum of even or odd
        digit = int(number_in_string[index])
        # checking whether the index is odd or even + adding the sum accordingly:
        if index % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
# printing the final result:
    if even_sum == odd_sum:
        print(number_in_string, end=" ")
