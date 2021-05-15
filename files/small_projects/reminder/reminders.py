import json
from menu import *


def main():

    try:
        with open("reminders.json") as f:
            reminders = json.load(f)
    except FileNotFoundError:
        reminders = []

    while True:
        menu()
        choice = get_int("Choose from menu: ")
        if choice == 1:
            reminder = input("Type reminder: ")
            reminders.append(reminder)
            with open("reminders.json", "w") as f:
                json.dump(reminders, f)

        elif choice == 2:
            reminder_index = get_int("Give index of the reminder: ") - 1
            reminders.pop(reminder_index)
            with open("reminders.json", "w") as f:
                json.dump(reminders, f)

        elif choice == 3:
            for i in range(len(reminders)):
                print(f"{i+1}. {reminders[i]}")

        elif choice == 4:
            print("Bye!")
            break


main()
