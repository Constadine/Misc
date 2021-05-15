a_list = [[0, 2, 3, 4], [5, 4, 3, 2], [10, 20, 30, 40]]

print(a_list)

a_list.insert(0, [0,0,0,0])
print(a_list)

for row in a_list:
    row.append(1)

print(a_list)