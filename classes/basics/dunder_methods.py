class Time:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return f"{str(self.hour).zfill(2)}:"\
            f"{str(self.minute).zfill(2)}:"\
            f"{str(self.second).zfill(2)}"\



t = Time(11, 2, 3)

print(t)
print("The time is " + str(t))
