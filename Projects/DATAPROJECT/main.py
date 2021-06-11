from menus import *
from pupils import Pupils
from teachers import Teachers
from lessons import Lessons


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
    lessons = Lessons()

    while True:

        menu()

        choice = get_int("Pick one: ")

        if choice == 1:

            pupils_menu()

            pupils_choice = get_int("Pick one: ")

            if pupils_choice == 1:
                print("NEW PUPIL")
                print("===========")
                pupil = pupils.create_pupil()
                if pupil is None:
                    continue
                else:
                    print("NEW PUPIL")
                    print(pupil)

            elif pupils_choice == 2:

                pupils_print_submenu()

                print_choice = get_int("Give your choice: ")

                if print_choice == 1:
                    pupil_id = get_int("Give id: ")
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Pupil does not exist (with this id)")
                    else:
                        print("   PUPIL   ")
                        print(pupil)
                elif print_choice == 2:
                    print(pupils)
                elif print_choice == 3:
                    pupils.print_pupils_names()
                else:
                    print("Wrong input! ")
                    continue

            elif pupils_choice == 3:

                pupils_update_submenu()

                update_choice = get_int("Give your choice: ")
                if update_choice == 1:
                    pupil_id = get_int("Give id: ")
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Error! There is no pupil with this id!")
                        continue
                elif update_choice == 2:
                    surname = input("Give surname: ")
                    matching_pupils = pupils.search_pupil_by_surname(surname)
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

                # pupil: update
                pupils.pupil_update(pupil)

            elif pupils_choice == 4:

                pupils_delete_submenu()

                delete_choice = get_int("Give your choice: ")

                if delete_choice == 1:
                    pupil_id = get_int("Give id: ")

                    pupil = pupils.search_pupil_by_id(pupil_id)
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

                pupils.delete_pupil_by_id(pupil_id, lessons)

        elif choice == 2:

            teachers_menu()

            teacher_choice = get_int("Pick one: ")

            if teacher_choice == 1:
                first_name = input("Give name: ")
                last_name = input("Give surname: ")
                teachers.create_teacher(first_name, last_name)
            elif teacher_choice == 2:
                teacher_id = get_int("Give id: ")
                teacher = teachers.read_teacher(teacher_id)
                if teacher is None:
                    print("No such teacher exists!")
                else:
                    print(teacher)
            elif teacher_choice == 3:
                teacher_id = get_int("Give id: ")
                teachers.update_teacher(teacher_id)
            elif teacher_choice == 4:
                teacher_id = get_int("Give id: ")
                teachers.delete_teacher(teacher_id, lessons)

        elif choice == 3:

            lessons_menu()

            lesson_choice = get_int("Pick one: ")

            if lesson_choice == 1:
                lesson_name = input("Give lesson name: ")
                lessons.create_lesson(lesson_name)
            elif lesson_choice == 2:
                lesson_id = get_int("Give id: ")
                lesson = lessons.read_lesson(lesson_id)
                if lesson is None:
                    print("No such lesson exists!")
                else:
                    lesson.print_lesson_details(teachers, pupils)
            elif lesson_choice == 3:
                lesson_id = get_int("Give id: ")
                lessons.update_lesson(lesson_id, teachers, pupils)
            elif lesson_choice == 4:
                lesson_id = get_int("Give id: ")
                lessons.delete_lesson(lesson_id)

        elif choice == 4:
            print("Bye bye!")
            pupils.save_pupils_data()
            teachers.save_teachers_data()
            lessons.save_lessons_data()
            break


main()
