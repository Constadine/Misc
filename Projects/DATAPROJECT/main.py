from menus import print_menu, print_submenu
from pupils import Pupils
from teachers import Teachers


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except:
            print("Wrong input!")
            continue
    return value


def main():

    pupils = Pupils()
    teachers = Teachers()

    while True:
        print_menu()
        choice = get_int("Pick one: ")

        if choice == 1:
            print("NEW PUPIL")
            print("==========")
            pupil = pupils.create_pupil()
            if pupil is None:
                continue
            else:
                print("NEW PUPIL CREATED")
                print(pupil)

        elif choice == 2:
            print_submenu()
            print_choice = get_int("Give your choice: ")

            if print_choice == 1:
                pupil_id = get_int("Give id:")
                pupil = pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil  with this id does not exist.")
                else:
                    print("   PUPIL   ")
                    print(pupil)

            elif print_choice == 2:
                print("\n")
                print(pupils)

            elif print_choice == 3:
                print("\n")
                pupils.print_pupils_names()

            else:
                print("Wrong input! ")
                continue

        elif choice == 3:
            print("\n===============")
            print("      SUB-MENU (UPDATE) ")
            print("1 - Update Pupil (search by id)")
            print("2 - Update Pupil (search by surname)")
            update_choice = get_int("Give your choice: ")

            if update_choice == 1:
                pupil_id = get_int("Give id: ")

                pupil = pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! No pupil with this id!")
                    continue

            elif update_choice == 2:
                last_name = input("Give surname: ")
                matching_pupils = pupil.search_pupil_by_surname(last_name)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print(p)
                        print(f"id = {p['id']}")
                        print("-" * 15)
                    pupil_id = get_int("Give id: ")
                    pupil = pupils.search_pupil_by_id(pupil_id)

            pupils.pupil_update(pupil)

        elif choice == 4:
            print("\n===============")
            print("      SUB-MENU (DELETE) ")
            print("1 - Delete Pupil (search by id)")
            print("2 - Delete Pupil (search by surname)")
            delete_choice = get_int("Give your choice: ")

            if delete_choice == 1:
                pupil_id = get_int("Give id: ")

                pupil = pupil.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! No pupil with this id!")
                    continue

            elif delete_choice == 2:
                last_name = input("Give surname: ")
                matching_pupils = pupils.search_pupil_by_surname(last_name)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print(p)
                        print(f"id = {p['id']}")
                        print("-" * 15)
                    pupil_id = get_int("Give id: ")
                    pupil = pupils.search_pupil_by_id(pupil_id)

            pupils.delete_pupil_by_id(pupil["id"])

        elif choice == 5:
            first_name = input("Give name: ")
            surname = input("Give surname: ")
            teachers.create_teacher(first_name, surname)
            print(teachers)

        elif choice == 6:
            teacher_id = get_int("Give id: ")
            teacher = teachers.read_teacher(teacher_id)
            if teacher is None:
                print("No such teacher exists!")
            else:
                print(teacher)

        elif choice == 7:
            teacher_id = get_int("Give id: ")
            teachers.update_teacher(teacher_id)

        elif choice == 8:
            teacher_id = get_int("Give id: ")
            teachers.delete_teacher(teacher_id)

        elif choice == 9:
            print("Bye.")
            teachers.save_teachers_data()
            pupils.save_pupils_data()
            break


main()
