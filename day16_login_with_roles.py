users = {
    "admin": {
        "password" : "1234",
        "role" : "admin" 
    
    },
    "student": {
        "password" : "abcd",
        "role" : "student"
    
    }
}

username = input("Enter username: ")
password = input("Enter password: ")
 
user_data = users.get(username)

if user_data:
    if password == user_data["password"]:
        print("login successful")

        if user_data["role"] == "admin":
           print("Welcome admin. You have full access.")
        elif user_data["role"] == "student":
           print("Welcome student. You have limited access.")

    else:
       print("login failed. Wrong password.")

else:
   print("login failed. Username not found.")