# use list coprehensions instead of for raw loops

squares = []
for i in range(11):
    squares.append(i**2)

print(squares)

squares = [i**2 for i in range(11)]
print(squares)
