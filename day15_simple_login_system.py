correct_username = "admin"
correct_password = "1234"

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print("Login failed")