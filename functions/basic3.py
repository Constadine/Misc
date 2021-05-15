# πώς να αλλαζω value immutable type

def f(arg):
    arg = 5
    return arg  # χρησιμοποιώ το return


x = 4
x += f(x)
print(x)
