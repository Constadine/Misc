def merge(name1, name2, name3):
    with open(name1) as f:
        content1 = f.read()

    with open(name2) as f:
        content2 = f.read()

    with open(name3, "a") as f:
        f.write(content1)
        f.write(content2)

# or


def merge2(name1, name2, name3):
    with open(name3, "w") as f:
        with open(name1) as g:
            contents = g.read()
        f.write(contents)

        with open(name2) as g:
            contents = g.read()
        f.write(contents)


merge("t1.txt", "t2.txt", "t3.txt")
