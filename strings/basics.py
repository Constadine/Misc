string = "Sample String"
print((string + " ") * 3)           # mult
print(string[1])                    # indexing
print(string[1:4] + string[-4:-1])  # slicing
print(len(string))                  # length
print(max("sample"))                # max
print(min("String"))                # min
print(string.index("am"))           # searching
print(string.count("S"))            # counting
# str[2] = "c"  not working..
new_str = string[:2] + "c" + string[3:]
print(new_str)


print("int: " + str(5))
print("float: " + str(5.1))
print("boolean: " + str(True))
print("list: " + str([1, 2]))
print("tuple: " + str((1, 2)))
print("set: " + str({1, 2}))
print("dict: " + str({1: 2, 3: 4}))

print(list("Find what you love and let it kill you."))

print(" ".join(["a", "b", "c"]))
print(", ".join({"a", "b", "c"}))
print(" # ".join({"a": 1, "k": 10}))

print(f"With a result: {1+4}")
x = 3
print(f"For debugging: {x=}")
mult_line = (
    f"multiline: {x} value\n"
    f"multiline: {x*x} square"
)
print(mult_line)
print(f"A float with 2 decimals: {1/3:.2}|")
print(f"A float with width 6: {1/4:6}|")
print(f"A float with width 6 and 2 decimals: {1/3:6.2}|")
print(f"An integer(hexadecimal): {155:x}")
print(f"An integer(octal): {155:o}")
print(f"An integer(scientific): {155:e}")
