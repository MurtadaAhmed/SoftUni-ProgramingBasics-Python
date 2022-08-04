# 1- outer cycle>> read the number while the command is not stop
# 2- inner cycle >> number % (all the numbers between 1 and the number itself) >> if we got 2 result with == 0 >>
# it meant the number is prime because it accept moduling on itself and number one only >> all the rest are non prime

command = input()
prime_sum = 0
non_prime_sum = 0
while command != "stop":
    command = int(command)  # converting into integer
    if command <0: # if the number is negative
        print("Number is negative.")
        command = input()  # this is to read a new command and to break the cycle one time my continue below
        continue
    count_module_zero = 0  # it should be exactly 2 if the number is prime
    for number in range(1, command + 1):
        if command % number == 0:
            count_module_zero += 1
    if count_module_zero == 2:  # which means prime number
        prime_sum += command
    else:
        non_prime_sum += command

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")