N = 100
evens = set()

for number in range(0, N+1, 2):
    evens.add(number)
print(evens)


odds = set()

for number in range(1, N+1, 2):
    odds.add(number)
print(odds)

mult3 = set()
for number in range(0, N, 3):
    mult3.add(number)
print(mult3)

primes = set()
for number in range(2, N+1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.add(number)

print(primes)

# αρτιοι ή πολλαπλασια του 3 
set1 = evens | mult3
print(set1)
# περιττοί πρώτοι
set2 = odds & primes
print(set2)
# πρώτοι αλλά όχι περιττοί
set3 = primes - odds
print(set3)
# περιττοί ή πρώτοι αλλά όχι ταυτόχρονα και περιττοί και πρώτοι
set4 = primes ^ odds
print(set4)
