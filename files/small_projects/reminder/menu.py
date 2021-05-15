

def menu():
    print("1. Add reminder")
    print("2. Remove reminder")
    print("3. Print reminder")
    print("4. Exit")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except:
            print("Wrong input!")
            continue
    return value
