from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())


N = 10
pupils = set()

for number in range(N):
    pupils.add("pupil" + str(number))

geo = ()
math = ()


def teams(sub):
    list_pupils = list(pupils)
    sub = set()
    for _ in range(N//2):
        pos1 = randrange(0, len(list_pupils))
        pupil1 = list_pupils.pop(pos1)
        pos2 = randrange(0, len(list_pupils))
        pupil2 = list_pupils.pop(pos2)
        team = (pupil1, pupil2)
        sub.add(team)
    print(sub)


teams(geo)
teams(math)
