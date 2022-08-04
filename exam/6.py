k = int(input())
l = int(input())
m = int(input())
n = int(input())
attempts = 1
for number1 in range(k, 9):
    for number2 in range(9,l - 1,-1):
        for number3 in range(m,9):
            for number4 in range(9,n - 1,-1):
                first_number = str(number1)+str(number2)
                second_number = str(number3)+str(number4)
                if number1 % 2 == 0 and number3 % 2 == 0 and number2 % 2 != 0 and number4 % 2 != 0 and attempts <= 6:
                    if first_number != second_number:
                        print(f"{number1}{number2} - {number3}{number4}")
                        attempts += 1
                    else:
                        print("Cannot change the same player.")


