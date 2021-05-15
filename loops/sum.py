Sum = 0

for i in range(10):
    Sum += int(input(f"Give the {i+1}th number: "))
    # print(f"We need {9-i} more numbers")

print("Their sum is: " + str(Sum))
