import json


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except:
            print("Wrong input!")
            continue
    return value


try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

while True:
    print("1. New user")
    print("2. Exit")
    choice = get_int("Pick one: ")
    if choice == 1:
        user = {}
        user["full_name"] = input("Give full name: ")
        user["username"] = input("Give username: ")
        user["password"] = input("Give password: ")
        user["role"] = input("Admin or user: ")

        users.append(user)

    elif choice == 2:
        with open("users.json", "w") as f:
            json.dump(users, f)
        break
    else:
        print("Wrong input!")
