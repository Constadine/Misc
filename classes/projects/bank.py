# from queue import Queue
from random import randrange, seed
from datetime import datetime


class Queue:
    def __init__(self) -> None:
        self.array = []

    def enqueue(self, elem):
        self.array.append(elem)

    def dequeue(self):
        if not self.array:
            return None
        else:
            return self.array.pop(0)

    def __str__(self) -> str:
        return ", ".join(self.array)

    def __add__(self, other):
        new_q = Queue()
        new_q.array = self.array[:]
        new_q.enqueue(other)
        return new_q

    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __neg__(self):
        return self.dequeue()

    def __len__(self):
        return len(self.array)


class Bank:
    def __init__(self, N) -> None:
        self.N = N
        self.cash_desks = [Queue() for i in range(N)]

    def customer_enters(self, full_name):
        cash_desk = randrange(self.N)
        self.cash_desks[cash_desk] += full_name
        print(full_name + " entered! To be served by cashdeask: " + str(cash_desk))

    def customer_served(self):
        not_empty_cash_desks = [i for i in range(
            self.N) if len(self.cash_desks[i]) > 0]

        if len(not_empty_cash_desks) > 0:
            cash_desk = not_empty_cash_desks[randrange(
                len(not_empty_cash_desks))]
            customer = - self.cash_desks[cash_desk]
            print(f"{customer} served by cash desk {cash_desk}")
        else:
            print("No customers.")

    def __str__(self) -> str:
        st = "\n" + "=" * 20
        for i in range(self.N):
            st += "\nCash Desk " + str(i) + ": "
            st += str(self.cash_desks[i])
        st += "\n" + "=" * 20
        return st


def main():
    seed(datetime.now())

    bank = Bank(3)

    for i in range(101):
        num = randrange(101)
        if num <= 30:
            bank.customer_served()
        else:
            bank.customer_enters("Cust" + str(randrange(1000)))

        if i % 10 == 0:
            print(bank)

    print("BANK CLOSED")


main()
