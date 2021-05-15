def input_integer():
    while True:
        data = input("Insert a digit: ")
        if data.isdigit():
            return int(data)
        else:
            print("Only digits please.")


def input_integer2():
    # insert integer + check for validity
    while True:
        try:
            integer = int(input("Insert an integer: "))
            return integer
        except:
            print("Only integers please!")


def input_float():
    while True:
        data = input("Give an float: ").strip()
        if "." in data:
            parts = data.split(".")
            if len(parts) > 2:
                print("Only one dot at most please.")
            elif parts[0].isdigit() and parts[1].isdigit():
                return float(data)
            else:
                print("Only digits please.")
        else:  # . not in data
            if data.isdigit():
                return float(data)
            else:
                print("Only digits please. ")


def input_float2():
    # insert integer + check for validity
    while True:
        try:
            floater = float(input("Insert a float: "))
            return floater
        except:
            print("Only floats please!")

    # return number
