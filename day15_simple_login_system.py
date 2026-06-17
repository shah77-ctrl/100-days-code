# Day 15 - Simple Login System
# This program checks username and password with 3 login attempts.

correct_username = "admin"
correct_password = "1234"

login_successful = False

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        login_successful = True
        break
    else:
        print("Login failed")

if not login_successful:
    print("Account locked")