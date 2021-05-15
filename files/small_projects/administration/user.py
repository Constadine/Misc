import json

try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

not_logged = True
while not_logged:
    user_username_input = input("Username: ")
    user_password_input = input("Password: ")
    for user in users:
        if user["username"] == user_username_input and user["password"] == user_password_input:
            if user["role"] == "user":
                print(f'Welcome {user["full_name"]}')
            else:
                print("Welcome Admin")
            not_logged = False
            break
        elif user["username"] == user_username_input and user["password"] != user_password_input:
            print("Wrong password.")
            break
    else:
        print("This username does not exist.")
