f = open("test.txt", "w")

f.write("Whassssup")

f.close()

with open("test2.txt", "w") as f:
    f.write("Texxxxxxxxt\n")
    f.write("and moreeee texxttt")

with open("test2.txt", "r") as f:
    contents = f.read()
    print(contents)


with open("test2.txt", "r") as f:
    for line in f:
        print(line)


with open("test2.txt", "r") as f:
    lines = f.readlines()
    print(lines)
