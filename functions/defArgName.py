
def print_name(first_name, surname, details=False, second_name="", second_surname=""):
    if details:
        if second_name != "":
            print(f"Fist Name: {first_name}-{second_name}")
        else:
            print(f"Fist Name: {surname}")
        if second_surname != "":
            print(f"Surname  : {surname} {second_surname}")
        else:
            print(f"Surname  : {surname}")
    else:
        if second_name != "":
            if second_surname != "":
                print(f"{first_name}-{second_name} {surname} {second_surname}")
            else:
                print(f"{first_name}-{second_name} {surname}")

        else:
            if second_surname != "":
                print(f"{first_name} {surname} {second_surname}")
            else:
                print(f"{first_name} {surname}")


print_name("Charles", "Vein", second_name="Dead")
