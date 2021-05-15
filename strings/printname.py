

while True:
    string = input("Give name: ")
    string = string.strip()

    if string.isalpha():
        name = string.capitalize()
        print(f"Name Entered: {name}")
        break
    else:
        print("chars only")
