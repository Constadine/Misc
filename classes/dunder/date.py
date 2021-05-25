class Time:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return f"{str(self.hour).zfill(2)}:"\
            f"{str(self.minute).zfill(2)}:"\
            f"{str(self.second).zfill(2)}"\


    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
        return False

    def __repr__(self) -> str:
        return f"Time({self.hour},{self.minute},{self.second})"


class Date:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"

    def __repr__(self) -> str:
        return f"Date({self.day},{self.month},{self.year})"

    def __eq__(self, other) -> bool:
        return self.day == other.day and self.month == other.month and self.year == other.year


class DateTime:
    def __init__(self, date, time) -> None:
        self.date = date
        self.time = time

    def __str__(self) -> str:
        return str(self.date) + " " + str(self.time)

    def __repr__(self) -> str:
        return f"DateTime({repr(self.date)},{repr(self.time)})"


d = Date(11, 1, 2020)
print(d, repr(d))


t = Time(11, 1, 1)

dt = DateTime(d, t)

print(dt, repr(dt))
