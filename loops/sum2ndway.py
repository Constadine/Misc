numbers = []

while len(numbers) < 10:
    numbers.append(int(input(f"Give the {len(numbers) +1}th number: ")))

print(f"Their sum is: {sum(numbers)}")