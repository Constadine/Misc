best = ["makoulas", "alkikos", "kronk"]

guests = ["bob", "tim", "makoulas", "martin", "alkikos", "jim", "kronk", "dave", "din", "joe"]

best_cnt = 0
for best_friend in best:
    if best_friend in guests:
        best_cnt += 1

if best_cnt < 2:
    print("Declined")
else:
    print("Approved")