def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True


def is_square(number):
    i = 0
    sq = 0
    while sq < number:
        i += 1
        sq = i * i

    return sq == number


def is_cube(number):
    i = 0
    cub = 0
    while cub < number:
        i += 1
        cub = i ** 3

    return cub == number


for i in range(1, 101):
    print(f"{i}: ", end=" ")
    if is_odd(i):
        print("Odd", end=" ")
    if is_even(i):
        print("Even", end=" ")
    if is_prime(i):
        print("Prime", end=" ")
    if is_square(i):
        print("Square", end=" ")
    if is_cube(i):
        print("Cube", end=" ")
    print("")
