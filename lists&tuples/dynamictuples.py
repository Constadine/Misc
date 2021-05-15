my_list = []

for i in range(10):
    number = int(input("Give a number: "))
    while number > 20 or number < 10:
        number = int(input("Give a number (10-20): "))
    my_list.append(number)

my_tuple = tuple(my_list)

list_squares = []
for i in range(10):
    list_squares.append(my_list[i]**2)

print(list_squares)

list_squares.sort()
tuple_squares = tuple(list_squares)