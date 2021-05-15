class Doggo:

    # members
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 4

    # methods
    def eat(self):
        self.mood += 1

    def bark(self):
        if self.mood > 5:
            print("Woof woof woof!")
        else:
            print("woof..")

    def walk(self):
        self.mood += 1


piko = Doggo("Piko", 10, "Terrier")
lassie = Doggo("Lassie", 30, "Colley")

for _ in range(2):
    piko.bark()
    piko.walk()
piko.bark()
piko.eat()
piko.bark()
