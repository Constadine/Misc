class Counter:
    def __init__(self) -> None:
        self.counter = 0

    def __str__(self):
        return str(self.counter)

    def __pos__(self):
        self.counter += 1

    def __neg__(self):
        self.counter -= 1


c = Counter()

+c
+c
+c
print(c)

-c
print(c)
