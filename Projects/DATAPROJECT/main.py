from mod_pupils import *
from mod_teachers import *


def main():
    init_teachers_data()
    init_pupils_data()
    while True:
        print_menu()
        choice = get_int("Pick one: ")

        if choice == 1:
            print("NEW PUPIL")
            print("==========")
            pupil = create_pupil()
            if pupil is None:
                continue
            else:
                print("NEW PUPIL CREATED")
                print_pupil(pupil)

        elif choice == 2:
            print_submenu()
            print_choice = get_int("Give your choice: ")

            if print_choice == 1:
                pupil_id = get_int("Give id:")
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil  with this id does not exist.")
                else:
                    print("   PUPIL   ")
                    print_pupil(pupil)

            elif print_choice == 2:
                print("\n")
                print_pupils_details()

            elif print_choice == 3:
                print("\n")
                print_pupils_names()

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

                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! No pupil with this id!")
                    continue

            elif update_choice == 2:
                surname = input("Give surname: ")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(p)
                        print(f"id = {p['id']}")
                        print("-" * 15)
                    pupil_id = get_int("Give id: ")
                    pupil = search_pupil_by_id(pupil_id)

            pupil_update(pupil)
            print("Pupil updated!")

        elif choice == 4:
            print("\n===============")
            print("      SUB-MENU (DELETE) ")
            print("1 - Delete Pupil (search by id)")
            print("2 - Delete Pupil (search by surname)")
            delete_choice = get_int("Give your choice: ")

            if delete_choice == 1:
                pupil_id = get_int("Give id: ")

                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! No pupil with this id!")
                    continue

            elif delete_choice == 2:
                surname = input("Give surname: ")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(p)
                        print(f"id = {p['id']}")
                        print("-" * 15)
                    pupil_id = get_int("Give id: ")
                    pupil = search_pupil_by_id(pupil_id)

            delete_pupil_by_id(pupil["id"])
            print("Pupil deleted!")

        elif choice == 5:
            first_name = input("Give name: ")
            surname = input("Give surname: ")
            create_teacher(first_name, surname)
            print(teachers)

        elif choice == 6:
            teacher_id = get_int("Give id: ")
            teacher = read_teacher(teacher_id)
            print_teacher(teacher)

        elif choice == 7:
            teacher_id = get_int("Give id: ")
            teacher_key = input("Give key: ")
            teacher_value = input("Give value: ")
            update_teacher(teacher_id, teacher_key, teacher_value)

        elif choice == 8:
            teacher_id = get_int("Give id: ")
            delete_teacher(teacher_id)
            print(teachers)

        elif choice == 9:
            print("Bye.")
            save_teachers_data()
            save_pupils_data()
            break


main()
