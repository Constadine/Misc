# immutable.arguments.py
# def f(arg):
#     print(arg)
#     print(f"id arg={id(arg)}")
#     arg = "Change!"
#     print(arg)
#     print(f"id arg={id(arg)}")


# s = "Initial"
# print(s)
# print(f"id s={id(s)}")
# f(s)
# print(s)
# print(f"id s={id(s)}")


# def f(arg):
#     print(arg)
#     print(f"id arg={id(arg)}")
#     arg.append(3)  # μπορώ να κανω τετοιες αλλαγες
#     print(arg)
#     print(f"id arg={id(arg)}")


# l = [1, 2]
# print(l)
# print(f"id l={id(l)}")
# f(l)
# print(l)
# print(f"id l={id(l)}")

def f(arg):
    global l
    print(arg)
    print(f"id arg={id(arg)}")
    arg = 2  # αλλά οχι τετοιες
    print(arg)
    print(f"id arg={id(arg)}")


l = 1
print(l)
print(f"id l={id(l)}")
f(l)
print(l)
print(f"id l={id(l)}")
