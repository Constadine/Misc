class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.__hunger = hunger  # 2 underscore

    def express(self):
        if self.hunger > 5:
            print("Moooooooooooowwww")
        else:
            print("Mowww")
