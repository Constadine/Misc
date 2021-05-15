from random import randrange, seed
from datetime import datetime

seed(datetime.now())

my_list = [randrange(0, 101) for _ in range(1501)]

with open("numbers.txt", "w+") as f:
    f.write(str(my_list))
