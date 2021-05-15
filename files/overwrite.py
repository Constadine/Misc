with open("overwrite.txt", "w") as f:  # overwrites all text in file
    f.write("Sample string")


with open("overwrite.txt", "a") as f:   # appends text in file
    f.write("Sample string")
