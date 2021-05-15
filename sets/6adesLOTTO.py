from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())


def randoms(x, y):
    while True:
        rand_number = randrange(x, y)
        if rand_number not in column:
            column.add(rand_number)
            break


i = 0
columns = []
while True:
    column = set()
    rand_number = randrange(10, 20)
    while len(column) < 6:
        if len(column) < 2:
            randoms(10, 20)
        elif len(column) < 4:
            randoms(20, 40)
        elif len(column) == 5:
            rand_number = 2*randrange(1, 5)
            column.add(rand_number)
        else:
            rand_number = randrange(41, 50, 2)
            column.add(rand_number)
    if column not in columns:
        columns.append(column)
        i += 1
        if i == 10:
            break

for column in columns:
    print(column)
