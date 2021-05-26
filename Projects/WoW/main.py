from character import Character
from arena import Arena
from random import randrange, seed, uniform
from datetime import datetime
from equipment import Equipment
from tank import Tank
from mage import Mage


def main():
    seed(datetime.now())

    orcs = [Character("Orc-" + str(i + 1),Equipment(uniform(1.1, 1.5), uniform(1.1,1.3)), 2, randrange(4))
            for i in range(5)]
    orcs += [Tank("Orc Tank" + str(i + 1),Equipment(uniform(1.1, 1.5), uniform(1.1,1.3)), 2, randrange(4))
            for i in range(5)]
    night_elves = [Character("Night Elf" + str(i + 1), Equipment(uniform(1.1,1.5), uniform(1.1,1.3)),
                             3, randrange(3)) for i in range(3)]
    night_elves += [Mage("Night Elf Mage" + str(i + 1),Equipment(uniform(1.1, 1.5), uniform(1.1,1.3)), 2, randrange(4))
            for i in range(5)]

    a = Arena(orcs, night_elves)
    a.play()



main()


