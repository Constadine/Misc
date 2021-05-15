# immutable.arguments.py
def f(arg):
    print(arg)
    arg = "Change!"
    print(arg)


s = "Initial"
print(s)
f(s)
print(s)


def f(arg):
    print(arg)
    arg.append(3)  # μπορώ να κανω τετοιες αλλαγες
    print(arg)


l = [1, 2]
print(l)
f(l)
print(l)


def f(arg):
    print(arg)
    arg = [3]  # αλλά οχι τετοιες
    print(arg)


l = [1, 2]
print(l)
f(l)
print(l)
