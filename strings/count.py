string = "I guess the only time most people think in justice is when it happens to them."

letters = set(string)
dictionary = {letter: 0 for letter in letters}


for char in string:
    dictionary[char] += 1

for key in sorted(dictionary.keys()):
    print(f"{key} : {dictionary[key]}")
