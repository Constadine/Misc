N = 5
A = set()

for i in range(1, N+1):
    A.add(i)

# or
# C = [i for i in range(1, N+1)]
# A = set(C)


B = set()
for elem in A:
    B.add((elem, elem**2))


print(B)
