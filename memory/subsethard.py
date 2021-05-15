subsets = set()
subsets.add(frozenset())

N = 4

for i in range(1, N+1):
    new_subsets = set()
    for subset in subsets:
        nonfz = set(subset)
        nonfz.add(i)
        fz = frozenset(nonfz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person(35, 36)

print(p1.name)
print(p1.age)
