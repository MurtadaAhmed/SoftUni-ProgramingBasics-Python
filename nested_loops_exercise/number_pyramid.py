number = int(input())
counter = 1  # we will print the counter number instead of the number entered above
for row in range (1, number + 1):  # this will repeat 1 - number
    for column in range (1, row + 1):  # this will repeat 1 - number of rows(to create the number of columns)
        if counter > number:
            break  # this is to break the inner circle when the counter > number
        print(counter, end=" ")
        counter += 1
    if counter > number:
        break  # this is to break the outer circle when the counter > number, otherwise it will keep printing empty
        # lines due to the print line below
    print()
