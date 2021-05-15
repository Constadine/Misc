def my_sum(*numbers):
    print(numbers)
    s = 0
    for number in numbers:
        print(number)
        s += int(number)
    return s


print(f"sum = {my_sum(1,2,3,4,5)}")


def float_average(*numbers):
    s = 0
    for number in numbers:
        s += number
    return s/len(numbers)


print(float_average(2.1, 4.2, 5.9, 7.8))

# kwargs


def create_person(**kwargs):
    print(kwargs)
    return kwargs


create_person(name="Jimin", band="BTS")
create_person(name="Jin", band="BTS")
