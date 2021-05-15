numbers = [5, 3, 7, 15, 0, 35, 33]

Max = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > Max:
        Max = numbers[i]

print(Max)