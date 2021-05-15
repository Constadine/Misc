def break_da_numba(numba):
    number = str(numba)
    first = number[0]
    second = number[1]
    third = number[2]
    print(f"""
    1st digit: {first}
    2nd digit: {second}
    3rd digit: {third} 
    """)

# o r


def digit_print(number):
    third = number % 10
    number = number // 10
    second = number % 10
    fist = number // 10
    print(f"1st digit: {first}")
    print(f"2st digit: {second}")
    print(f"3st digit: {third}")
