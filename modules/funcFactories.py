def factory_power(power):
    def nth_power(number):
        return number**power  # to value του power εχει αρχικοποιηθεί ως parameter

    return nth_power  # return the nested function


square = factory_power(2)
print(square(4))

cube = factory_power(3)
print(cube(4))
