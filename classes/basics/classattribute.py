class C:
    counter = 0  # έχω πρόσβαση σε όλο το πρόγραμμα

    def __init__(self) -> None:
        C.counter += 1


o1 = C()
o2 = C()

print(C.counter, o1.counter, o2.counter)
