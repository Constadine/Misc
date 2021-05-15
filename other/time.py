hours = int(input("Δώσε ώρες: "))
minutes = int(input("...λεπτά: "))
seconds = int(input("...και δευτερόλεπτα: "))

if hours < 10:
    hours = "0" + str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)

if seconds < 10:
    seconds = "0" + str(seconds)

print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
