from abc import ABC, abstractmethod
from random import randrange, seed
from datetime import datetime

class Person(ABC):
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        self.served_cnt = 0

    def report(self):
        print(f"{self.name} served {self.served_cnt} customers.")

class Waiter(Person):
    def __init__(self, name, salary) -> None:
        Person.__init__(self,name, salary)

    def serve(self, customers, barista):
        self.served_cnt += customers
        print(f"Waiter {self.name} served {customers} customers")
        barista.prepare(customers)

class Barista(Person):
    def __init__(self, name, salary) -> None:
        Person.__init__(self,name, salary)

    def prepare(self, customers):
        print(f"Barista {self.name} served {customers} customers")

        self.served_cnt += customers 

class Owner(Waiter,Barista):
    def __init__(self, name, salary) -> None:
        # Waiter.__init__(self,name, salary)
        # Barista.__init__(self,name, salary) den xreiazontai afou einai idies me to person
        Person.__init__(self,name,salary)

def main():
    o = Owner("owner", 1000)
    w1 = Waiter("waiter-1", 2000)
    w2 = Waiter("waiter-2", 2000)
    b = Barista("barista", 3000)

    waiters = [o,w1,w2]

    baristas = [o,b]
    for _ in range(11):
        waiters[randrange(3)].serve(randrange(1,5+1), baristas[randrange(2)])


    print("In total\n" + "-"*20)
    o.report()
    w1.report()
    w2.report()
    b.report()

main()