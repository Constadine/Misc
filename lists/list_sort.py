numbers = []
for i in range(3):
    number = float(input(f"Δώσε τον {i+1}o πραγματικό: "))
    numbers.append(number)

numbers.sort()
print(numbers)