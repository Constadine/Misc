# Default arguments:
# default value που θα παρει το argument αν δε δηλώσω εγώ διαφορετικό όρισμα

def func_args(integer1=2):
    result = integer1 * integer1
    return result


print(func_args())
print(func_args(10))


def print_name(first_name, surname, details=False):
    if details:
        print(f"Fist Name: {first_name}")
        print(f"Fist Name: {surname}")
    else:
        print(f"{first_name} {surname}")


print_name("Charles", "Vein")
print_name("Charles", "Vein", True)
