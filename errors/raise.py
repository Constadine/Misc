while True:
    try:
        x = int(input("Give nonnegative inger: "))
        if x < 0:
            raise ValueError("NonNegative Value entered")
    except ValueError as v:
        print(v)
    else:
        print(x)
        break
