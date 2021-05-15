import json

pupils = []


def print_menu():
    print("\n===============")
    print("      MENU      ")
    print("1 - Create Pupil")
    print("2 - Print")
    print("3 - Update Pupil")
    print("4 - Delete Pupil")
    print("5 - Create Teacher")
    print("6 - Read Teacher")
    print("7 - Update Teacher")
    print("8 - Delete Teacher")

    print("9 - Exit")


def print_submenu():
    print("\n===============")
    print("      SUB-MENU (PRINT) ")
    print("1 - Print Pupil")
    print("2 - Print all pupils (details)")
    print("3 - Print all pupils (names)")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except:
            print("Wrong input!")
            continue
    return value


def init_pupils_data():
    global pupils
    try:
        with open("pupils.json") as f:
            pupils = json.load(f)
    except FileNotFoundError:
        pupils = []


def save_pupils_data():
    with open("pupils.json", "w") as f:
        json.dump(pupils, f)


def print_pupil(pupil):
    print(f"Name           : {pupil['name']}")
    print(f"Surame         : {pupil['surname']}")
    print(f"Father's name  : {pupil['fathersname']}")
    print(f"Age            : {pupil['age']}")
    print(f"Class          : {pupil['class']}")
    if "id_number" in pupil:
        print(f"ID card number : {pupil['id_number']}")


def next_id():
    if not pupils:
        return 1001
    else:
        ids = []
        for p in pupils:
            ids.append(p["id"])
        return max(ids) + 1


def create_pupil():
    name = input("Give name: ")
    surname = input("Give surname: ")
    fathersname = input("Give father's name: ")

    for p in pupils:
        if name == p["name"] and surname == p["surname"] and fathersname == p["fathersname"]:
            print("This pupil already exists.")
            ch = input("Do you want to continue? (y-yes, n-no): ")
            if ch == "n":
                return None

    age = get_int("Give age: ")
    pupil_class = get_int("Give class: ")
    id_card = input("Does he/she has an id card: (y-yes, n-no): ")
    if id_card == "y":
        id_number = input("give id card number: ")
    pupil = {}
    pupil["name"] = name
    pupil["surname"] = surname
    pupil["fathersname"] = fathersname
    pupil["age"] = age
    pupil["class"] = pupil_class
    if id_card == "y":
        pupil["id_number"] = id_number

    pupil["id"] = next_id()

    pupils.append(pupil)
    return pupil


def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)


def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            return pupil
    return None


def pupil_update(pupil):
    print_pupil(pupil)
    print("=" * 15)
    print("1-name")
    print("2-surname")
    print("3-father's name")
    print("4-age")
    print("5-class")
    print("6-id number")
    print("=" * 15)
    update_choice = get_int("Pick something to update: ")
    if update_choice == 1:
        pupil["name"] = input("Give new name: ")
    elif update_choice == 2:
        pupil["surname"] = input("Give new surname: ")
    elif update_choice == 3:
        pupil["fathersname"] = input("Give new father's name: ")
    elif update_choice == 4:
        pupil["age"] = get_int("Give age: ")
    elif update_choice == 5:
        pupil["class"] = input("Give new class: ")
    elif update_choice == 6:
        pupil["id_number"] = input("Give new id number: ")

    print("=" * 15)
    print_pupil(pupil)
    print("Pupil updated!")


def delete_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            pupils.remove(pupil)
            return


def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil["surname"]:
            match_pupils.append(pupil)
    return match_pupils


def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['fathersname'][0]}. {pupil['surname']}")
