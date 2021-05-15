n = int(input("Give a number between 3-20."))
numbers = []

while n < 3 or n > 20:
    n = int(input("I said between 3-20..."))

for i in range(n):
    numbers.append(int(input(f"Give {i+1}th number: ")))

numbers.sort()

print(numbers)