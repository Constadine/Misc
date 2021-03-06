# Multiple Inheritance

class King:
    def __init__(self, realm) -> None:
        self.realm = realm

    def rule(self):
        print("Now, I rule")


class Philosopher:
    def __init__(self, school) -> None:
        self.school = school

    def think(self):
        print("Now, I think")


class PhilosopherKing(King, Philosopher):
    def __init__(self, realm, school) -> None:
        King.__init__(self, realm)
        Philosopher.__init__(self, school)

    def routine(self):
        self.think()
        self.rule()
        self.think()


marcus_aurelius = PhilosopherKing("Roman Empire", "Stoic")
marcus_aurelius.routine()
