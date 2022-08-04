user_name = input()
correct_password = input()
second_password = input()
while second_password != correct_password:
    second_password = input()
print(f"Welcome {user_name}!")