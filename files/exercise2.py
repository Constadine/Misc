with open("test2.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].rstrip()

print(lines)
