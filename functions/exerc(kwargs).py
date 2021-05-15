def print_details(*args, **kwargs):
    print(kwargs)
    s = 0
    for grade in args:
        s += int(grade)
    average = s/len(args)
    print(average)
    dictionary = {}
    for key, value in kwargs.items():
        if value in dictionary:
            dictionary[value] += [key]
        else:
            dictionary[value] = [key]
    print(dictionary)


print_details(5, 7, 13, Banner="Math", Kane="Math", Stark="Programming")
