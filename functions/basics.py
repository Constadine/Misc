# Η return τερματίζει τη συνάρτηση:

def is_odd(number):
    if number % 2 == 1:
        return True
    return False


proof = is_odd(3)
print(proof)

# Δύναται αποθήκευση παραπάνω από μία τιμών:


def square_cube(number):
    return number**2, number**3


num = 5
square, cube = square_cube(num)

print(f"{num}^2={square}, {num}^3={cube}")

# Επιστροφή None:


def f():
    return


ret = f()
print(f"{ret}, {type(ret)}")


# Είδη μεταβλητών

def f():  # local
    global x  # χωρίς αυτό το x θα έμενα στο local scope της function οπότε θα εμφανιζόταν ως 3 μόνο όταν έτρεχα τη συνάρτηση
    x = 3
    print(x)


x = 2  # global
f()
print(x)

# Οργάνωση:

# constants
PI = 3.14
# globals
deck = {("ace", "spade")}

# functions


def f():
    print("somethin")


def g():
    print("smth else")


# main
def main():
    f()
    g()


main()


#
