class Cow:
    # H init = constructor. panta self prota.
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print("Moooooooooooowwww")
        else:
            print("Mowww")


molly = Cow(500, 10)
print(type(molly))
print(molly.hunger)
molly.express()
