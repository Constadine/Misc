with open("kinglear.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i].isupper():
        lines[i] = "\n" + lines[i] + "\n"
    else:
        lines[i] = "\t" + lines[i]

with open("kinglear2.txt", "w") as f:
    for line in lines:
        f.write(line)
