class X():
    def __init__(self) -> None:
        self.ar = [x for x in range(5)]
        self.other = 2

    def __len__(self):
        return len(self.ar)

    def __getitem__(self, item):
        return self.ar[item]


obj = X()
for item in obj:
    print(item)
