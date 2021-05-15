int_set = {1, 2, 3}
collection = {"hi", 3.14, True}
empty_set = set()
dublicates = {1, 2, 3, 1, 1, 2}

x = 4

my_set = {x, x**3, (x*3)}


# comprehensions

loop_set = set()
for i in range(2):
    for j in range(3):
        loop_set.add((i, j))

# γίνεται :

comp_set = {(i, j) for i in range(2) for j in range(3)}  # + if αν χρειάζεται
