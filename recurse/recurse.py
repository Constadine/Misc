n, m = 5, 15


def recurse(x, y):
    if x >= y:
        return x, y
    else:
        return recurse(x + 2, y + 1)


print(recurse(n, m))


def norecurse(x, y):
    while x < y:
        x += 2
        y += 1
    return x, y


print(norecurse(n, m))
