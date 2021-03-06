from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class HimalayanCat(Cat):
    def make_sound(self):
        super().make_sound()
        print("Miouw miouw")


class Dog(Animal):
    def make_sound(self):
        print("Woof woof")


class Doberman(Dog):
    pass


class KingDoberman(Doberman):
    def make_sound(self):
        super().make_sound()
        print("WOOAAAAAAAAF")


# Animal().make_sound() afirimeni class
Cat().make_sound()
HimalayanCat().make_sound()
Dog().make_sound()
Doberman().make_sound()
KingDoberman().make_sound()
